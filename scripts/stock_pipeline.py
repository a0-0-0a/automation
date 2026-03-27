import os
import sys
import random
import time
import glob
import importlib
import subprocess

# ════════════════════════════════════════════════════════════
# إعداد المسارات — نجلب الـ engine والـ groups من الـ scripts repo
# ════════════════════════════════════════════════════════════
SCRIPT_DIR        = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_REPO_PATH = os.environ.get("SCRIPTS_REPO_PATH", os.path.join(SCRIPT_DIR, "..", "scripts_repo"))
IMGS_DIR          = os.path.join(SCRIPT_DIR, "..", "imgs")

# أضف الـ private repo للـ path حتى نستورد منه
if SCRIPTS_REPO_PATH not in sys.path:
    sys.path.insert(0, SCRIPTS_REPO_PATH)

# ════════════════════════════════════════════════════════════
# استيراد الـ engine modules
# ════════════════════════════════════════════════════════════
from engine.filter       import passes_filter, sanitize_place_names
from engine.llm_client   import get_llm7_output
from engine.image_gen    import generate_image
from engine.local_builder import generate_local_data, build_local_prompt
from engine.seo_builder  import build_local_seo
from engine.repo_manager import (
    get_next_slot, get_total_generated, push_repo
)

# ════════════════════════════════════════════════════════════
# إعدادات
# ════════════════════════════════════════════════════════════
PIXAZO_KEY       = os.environ.get("PIXAZO_KEY", "")
GH_TOKEN         = os.environ.get("GH_TOKEN", "")
GH_USERNAME      = os.environ.get("GH_USERNAME", "a0-0-0a")

IMAGES_PER_REPO  = 333
TOTAL_REPOS      = 30
PUSH_EVERY       = 10
IMAGES_PER_RUN   = 180
SLEEP_BETWEEN    = 5
SLEEP_ON_FAIL    = (20, 40)

WEIGHTED_GROUPS = {
    "golden_sky":          4,
    "dramatic_clouds":     4,
    "glacial_lakes":       3,
    "waterfalls_rivers":   3,
    "granite_peaks":       3,
    "limestone_peaks":     3,
    "saharan_dunes":       2,
    "dramatic_sea_cliffs": 2,
    "beach_seascape":      2,
    "temperate_forest":    2,
    "wildflower_meadow":   2,
}

# ════════════════════════════════════════════════════════════
# تحميل الـ groups
# ════════════════════════════════════════════════════════════
def load_all_groups():
    all_groups = {}
    groups_dir = os.path.join(SCRIPTS_REPO_PATH, "groups")
    if SCRIPTS_REPO_PATH not in sys.path:
        sys.path.insert(0, SCRIPTS_REPO_PATH)
    for filepath in glob.glob(os.path.join(groups_dir, "group_*.py")):
        module_name = "groups." + os.path.basename(filepath)[:-3]
        try:
            mod = importlib.import_module(module_name)
            if hasattr(mod, "GROUPS"):
                all_groups.update(mod.GROUPS)
                print(f"   ✅ {os.path.basename(filepath)}: {len(mod.GROUPS)} groups")
        except Exception as e:
            print(f"   ⚠️ failed {os.path.basename(filepath)}: {e}")
    return all_groups

def pick_weighted_group(all_groups):
    weighted = []
    for name in all_groups:
        weight = WEIGHTED_GROUPS.get(name, 1)
        weighted.extend([name] * weight)
    return random.choice(weighted)

# ════════════════════════════════════════════════════════════
# تحميل SEO
# ════════════════════════════════════════════════════════════
def load_seo_module():
    try:
        from seo_data.seo_titles import generate_seo_title, get_seo_data
        print(f"   📂 SEO titles module loaded ✅")
        return generate_seo_title, get_seo_data
    except Exception as e:
        print(f"   ⚠️ SEO titles module not found: {e}")
        return None, None

# ════════════════════════════════════════════════════════════
# حفظ الـ txt
# ════════════════════════════════════════════════════════════
def save_txt(txt_path, seo, group_name, season, mood, label,
             source, prompt_source, seo_source):
    filename = os.path.basename(txt_path).replace(".txt", "")
    content = f"""TITLE:
{seo['title']}

DESCRIPTION:
{seo['description']}

CATEGORY:
{seo['category']}

KEYWORDS:
{seo['keywords']}

ORIENTATION:
{seo['orientation']}

MEDIA TYPE:
{seo['media_type']}

--- METADATA ---
GROUP: {group_name}
SEASON: {season}
MOOD: {mood}
LABEL: {label}
IMAGE SOURCE: {source}
PROMPT SOURCE: {prompt_source}
SEO SOURCE: {seo_source}
FILE: {filename}.png
"""
    os.makedirs(os.path.dirname(txt_path), exist_ok=True)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(content)

# ════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════
if __name__ == "__main__":

    print("=" * 60)
    print("  Stock Image Generator — GitHub Actions")
    print("=" * 60)

    print("  Loading groups...")
    ALL_GROUPS = load_all_groups()
    print(f"  Total groups: {len(ALL_GROUPS)}")

    print("  Loading SEO module...")
    GEN_TITLE, GET_SEO = load_seo_module()

    if not ALL_GROUPS:
        print("❌ No groups found!")
        exit(1)

    total_generated = get_total_generated(IMGS_DIR, TOTAL_REPOS)
    total_capacity  = IMAGES_PER_REPO * TOTAL_REPOS

    print(f"  Generated so far  : {total_generated}")
    print(f"  Total capacity    : {total_capacity}")
    print(f"  Remaining capacity: {total_capacity - total_generated}")
    print(f"  Images this run   : {IMAGES_PER_RUN}")
    print(f"  Repos             : {TOTAL_REPOS} × {IMAGES_PER_REPO} = {total_capacity}")
    print(f"  Push every        : {PUSH_EVERY}")
    print("=" * 60)

    if total_generated >= total_capacity:
        print("✅ All images already generated!")
        exit(0)

    success        = 0
    fail           = 0
    since_push     = 0
    modified_repos = set()

    while success < IMAGES_PER_RUN:

        repo_num, img_num, repo_dir = get_next_slot(IMGS_DIR, TOTAL_REPOS, IMAGES_PER_REPO)
        if repo_num is None:
            print("✅ All repos full — done!")
            break

        print(f"\n   ── [repo{repo_num}/{img_num} | run:{success+1}/{IMAGES_PER_RUN}] ──")

        try:
            base_data, label = generate_local_data(ALL_GROUPS, pick_weighted_group)
            group_name = base_data["group_name"]
            season     = base_data["season"]
            mood       = base_data["mood"]
            keywords   = ALL_GROUPS[group_name].get("stock_keywords", [])
            print(f"   📋 {label}")

            # ── LLM7 مع smart fallback ──
            # نولّد prompt محلي أولي
            initial_prompt_data = base_data.copy()
            llm_output, used_fallback_prompt = get_llm7_output(
                base_data, keywords, ALL_GROUPS, pick_weighted_group
            )

            # ── تحديد مصادر الـ prompt والـ SEO ──
            if llm_output:
                final_prompt      = llm_output["prompt"]
                prompt_source     = "llm7"
                txt_fallback      = False   # النص من LLM7 → لا x على الـ txt
                seo = {
                    "title":       llm_output["title"],
                    "description": llm_output["description"],
                    "category":    llm_output["category"],
                    "keywords":    llm_output["keywords"],
                    "orientation": "Horizontal",
                    "media_type":  "Photography",
                }
                seo_source = "llm7"
            else:
                print(f"   📝 Building local prompt (fallback)...")
                final_prompt  = build_local_prompt(base_data)
                prompt_source = "local"
                txt_fallback  = True   # النص local → x على الـ txt
                print(f"   📝 Building local SEO (fallback)...")
                seo        = build_local_seo(group_name, season, mood, keywords, GEN_TITLE, GET_SEO)
                seo_source = "seo_titles"

            # ── أسماء الملفات ──
            # txt → x إذا كان الـ prompt محلياً (txt_fallback)
            # img → x إذا فشل Pixazo ورجعنا لـ Pollinations (img_fallback)
            txt_suffix = "x" if txt_fallback else ""
            img_path_base = os.path.join(repo_dir, "images", f"{img_num}")
            txt_path_base = os.path.join(repo_dir, "texts",  f"{img_num}{txt_suffix}")

            os.makedirs(os.path.join(repo_dir, "images"), exist_ok=True)
            os.makedirs(os.path.join(repo_dir, "texts"),  exist_ok=True)

            # generate_image يرجع (source, img_fallback)
            source, img_fallback = generate_image(
                final_prompt,
                img_path_base,
                prompt_source,
                PIXAZO_KEY
            )

            # الـ img suffix يُحدَّد بعد التوليد
            img_suffix = "x" if img_fallback else ""
            # أعد تسمية الصورة إذا كانت fallback
            actual_img_path = img_path_base + img_suffix + ".png"
            temp_img_path   = img_path_base + ".png"
            if img_fallback and os.path.exists(temp_img_path):
                os.rename(temp_img_path, actual_img_path)
            elif not img_fallback and os.path.exists(temp_img_path):
                pass  # الاسم صحيح بالفعل

            txt_path = txt_path_base + ".txt"
            save_txt(txt_path, seo, group_name, season, mood,
                     label, source, prompt_source, seo_source)

            success += 1
            since_push += 1
            modified_repos.add(repo_num)

            tags = []
            if txt_fallback: tags.append("TXT-FALLBACK ⚠️")
            if img_fallback: tags.append("IMG-FALLBACK ⚠️")
            tag_str = " [" + " | ".join(tags) + "]" if tags else ""

            print(f"   ✅ repo{repo_num}/{img_num} | img:{source} | prompt:{prompt_source}{tag_str}")
            print(f"   📌 {seo['title'][:55]}")

            if since_push >= PUSH_EVERY:
                push_repo(repo_num, IMGS_DIR)
                since_push = 0

            time.sleep(SLEEP_BETWEEN)

        except Exception as e:
            fail += 1
            wait = random.randint(SLEEP_ON_FAIL[0], SLEEP_ON_FAIL[1])
            print(f"   ❌ Failed: {e}")
            print(f"   ⏳ Waiting {wait}s...")
            time.sleep(wait)

    # final push
    print(f"\n   📤 Final push for modified repos...")
    for rn in modified_repos:
        push_repo(rn, IMGS_DIR)

    final_total = get_total_generated(IMGS_DIR, TOTAL_REPOS)
    print("\n" + "=" * 60)
    print(f"✅ Run complete!")
    print(f"   This run: {success} ✅ | {fail} ❌")
    print(f"   Total generated: {final_total} / {total_capacity}")
    print(f"   Remaining: {total_capacity - final_total}")
    print("=" * 60)
