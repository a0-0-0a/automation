import os
import random
import time
import requests
import glob
import importlib
import sys
import re
import subprocess
from urllib.parse import quote

# ════════════════════════════════════════════════════════════
# إعدادات
# ════════════════════════════════════════════════════════════
PIXAZO_KEY    = os.environ.get("PIXAZO_KEY", "")
GH_TOKEN      = os.environ.get("GH_TOKEN", "")
GH_USERNAME   = os.environ.get("GH_USERNAME", "a0-0-0a")

SCRIPT_DIR       = os.path.dirname(os.path.abspath(__file__))
IMGS_DIR         = os.path.join(SCRIPT_DIR, "..", "imgs")
IMAGES_PER_REPO  = 333
TOTAL_REPOS      = 30
PUSH_EVERY       = 10
IMAGES_PER_RUN   = 180
SLEEP_BETWEEN    = 5
SLEEP_ON_FAIL    = (20, 40)

# LLM7 retry settings
LLM7_API_RETRIES    = 3   # API connection retries
LLM7_FILTER_RETRIES = 5   # retries when filter blocks output

FORCED_PREFIX = (
    "Pure nature landscape photography only. "
    "Zero humans, zero people, zero faces, zero bodies. "
    "Zero animals, zero birds, zero insects, zero wildlife. "
    "Zero man-made objects, zero buildings, zero roads, zero vehicles, "
    "zero boats, zero planes, zero wires, zero signs, zero fences. "
    "Only untouched pure natural wilderness. "
)

FORCED_SUFFIX = (
    " Photorealistic RAW photography. Real existing location on Earth. "
    "Natural realistic colors only — no oversaturated, no neon, no fantasy. "
    "Natural sky only — blue daytime, warm golden hour only. "
    "Bright clear visibility throughout. "
    "8k ultra detailed. National Geographic quality. "
    "No humans. No animals. No man-made objects. "
    "No repeated patterns. Natural irregular organic shapes."
)

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
# قائمة أسماء الأماكن والدول للتنظيف والفلتر
# ════════════════════════════════════════════════════════════
ALL_PLACE_NAMES = [
    # دول
    "norway", "norwegian", "swiss", "switzerland", "france", "french",
    "italy", "italian", "germany", "german", "austria", "austrian",
    "canada", "canadian", "usa", "american", "australia", "australian",
    "brazil", "brazilian", "argentina", "chile", "peru", "bolivia",
    "russia", "russian", "china", "chinese", "japan", "japanese",
    "india", "indian", "nepal", "nepalese", "tibet", "tibetan",
    "mongolia", "mongolian", "iceland", "icelandic", "greenland",
    "alaska", "california", "colorado", "utah", "arizona",
    "patagonia", "patagonian", "croatia", "croatian",
    "jordan", "iran", "oman", "morocco", "moroccan",
    "kenya", "tanzania", "scotland", "scottish", "ireland", "irish",
    "wales", "england", "english", "spain", "spanish",
    "portugal", "portuguese", "turkey", "turkish", "greece", "greek",
    "saudi", "arabia", "uae", "emirates",
    # مناطق
    "sahara", "saharan", "alps", "alpine", "himalaya", "himalayan",
    "andes", "andean", "rockies", "dolomites", "amazon", "patagonian",
    "scandinavia", "scandinavian", "mediterranean", "caribbean",
    "atlantic", "pacific", "siberia", "siberian", "gobi",
    "kazakh", "kazakhstan", "appalachian", "tibetan",
    # أماكن محددة
    "banff", "yosemite", "plitvice", "namib", "atacama",
    "lofoten", "faroe", "azores", "fjord", "fiord",
    "eiger", "marmolada", "seceda", "lauterbrunnen",
    "skogafoss", "geiranger", "nærøyfjord", "reynisfjara",
    "cinque torri", "tre cime", "mont blanc",
    "denali", "wadi rum", "erg chebbi", "rub al khali",
    "big sur", "death valley", "moher", "etretat",
    "calanques", "santorini", "dalmatian", "smeralda",
    "abel tasman", "milford sound", "southern alps",
    "baikal", "achensee", "moraine", "louise",
    "borneo", "sabah", "daintree", "sumatra", "borneo",
    "muir woods", "tongass", "olympic", "appalachian",
    "białowieża", "bavarian", "black forest",
]

# الكلمات المحظورة في البروميت
FORBIDDEN_WORDS = [
    "human", "humans", "person", "persons", "people", "man", "men",
    "woman", "women", "child", "children", "boy", "girl",
    "figure", "figures", "face", "faces", "body", "bodies",
    "hand", "hands", "foot", "feet", "silhouette", "silhouettes",
    "footprint", "footstep", "hiker", "climber", "traveler",
    "tourist", "photographer", "observer", "visitor",
    "animal", "animals", "bird", "birds", "dog", "dogs",
    "cat", "cats", "fish", "insect", "insects", "bear", "bears",
    "wolf", "wolves", "deer", "horse", "horses", "cow", "cows",
    "sheep", "eagle", "eagles", "hawk", "hawks", "owl", "owls",
    "snake", "lizard", "frog", "butterfly", "butterflies",
    "bee", "bees", "ant", "ants", "fly", "worm", "moth", "moths",
    "whale", "dolphin", "shark", "seal", "fox", "rabbit",
    "squirrel", "wildlife", "creature", "creatures", "beast",
    "fauna", "flock", "herd", "nest", "web", "prey", "predator",
    "car", "cars", "truck", "trucks", "bus", "buses",
    "boat", "boats", "ship", "ships", "plane", "planes",
    "jet", "helicopter", "drone",
    "building", "buildings", "house", "houses", "tower", "towers",
    "bridge", "bridges", "road", "roads", "path", "trail", "trails",
    "fence", "fences", "wire", "wires", "pole", "poles",
    "sign", "signs", "statue", "statues", "monument", "ruins",
    "village", "villages", "city", "cities", "town", "towns",
    "farm", "farms", "cabin", "hut", "tent", "cairn",
    "structure", "structures", "infrastructure", "architecture",
    "shelter", "camp", "campsite",
] + ALL_PLACE_NAMES

def passes_filter(text):
    text_lower = text.lower()
    for word in FORBIDDEN_WORDS:
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, text_lower):
            return False, word
    return True, None

def sanitize_place_names(text):
    """يحذف أسماء الأماكن والدول من النص"""
    result = text
    for name in ALL_PLACE_NAMES:
        pattern = re.compile(r'\b' + re.escape(name) + r'\b', re.IGNORECASE)
        result = pattern.sub("", result)
    result = re.sub(r'\s+', ' ', result)
    result = re.sub(r',\s*,', ',', result)
    result = result.strip(' ,.-')
    return result

# ════════════════════════════════════════════════════════════
# تحميل seo_titles
# ════════════════════════════════════════════════════════════
def load_seo_module():
    if SCRIPT_DIR not in sys.path:
        sys.path.insert(0, SCRIPT_DIR)
    try:
        from seo_data.seo_titles import generate_seo_title, get_seo_data
        print(f"   📂 SEO titles module loaded ✅")
        return generate_seo_title, get_seo_data
    except Exception as e:
        print(f"   ⚠️ SEO titles module not found: {e}")
        return None, None

# ════════════════════════════════════════════════════════════
# إدارة الـ repos
# ════════════════════════════════════════════════════════════
def get_repo_count(repo_num):
    """عدد الصور في repo معين"""
    repo_dir = os.path.join(IMGS_DIR, f"img{repo_num}")
    if not os.path.exists(repo_dir):
        return 0
    nums = set()
    for f in os.listdir(repo_dir):
        if f.endswith(".png"):
            base = f.replace("x.png", "").replace(".png", "")
            if base.isdigit():
                nums.add(int(base))
    return len(nums)

def get_next_slot():
    """يرجع (repo_num, next_img_num, repo_dir) أو (None, None, None) إذا كل الـ repos ممتلئة"""
    for repo_num in range(1, TOTAL_REPOS + 1):
        repo_dir = os.path.join(IMGS_DIR, f"img{repo_num}")
        os.makedirs(repo_dir, exist_ok=True)

        existing_nums = set()
        for f in os.listdir(repo_dir):
            if f.endswith(".png"):
                base = f.replace("x.png", "").replace(".png", "")
                if base.isdigit():
                    existing_nums.add(int(base))

        count = len(existing_nums)
        if count < IMAGES_PER_REPO:
            next_num = max(existing_nums) + 1 if existing_nums else 1
            return repo_num, next_num, repo_dir

    return None, None, None

def get_total_generated():
    total = 0
    for repo_num in range(1, TOTAL_REPOS + 1):
        total += get_repo_count(repo_num)
    return total

# ════════════════════════════════════════════════════════════
# git push للـ repo
# ════════════════════════════════════════════════════════════
def push_repo(repo_num):
    repo_dir = os.path.join(IMGS_DIR, f"img{repo_num}")
    try:
        cmds = [
            ["git", "-C", repo_dir, "config", "user.email", "action@github.com"],
            ["git", "-C", repo_dir, "config", "user.name", "GitHub Action"],
            ["git", "-C", repo_dir, "add", "-A"],
        ]
        for cmd in cmds:
            subprocess.run(cmd, check=True, capture_output=True)

        result = subprocess.run(
            ["git", "-C", repo_dir, "status", "--porcelain"],
            capture_output=True, text=True
        )
        if not result.stdout.strip():
            return

        subprocess.run(
            ["git", "-C", repo_dir, "commit", "-m", "add images"],
            check=True, capture_output=True
        )
        subprocess.run(
            ["git", "-C", repo_dir, "checkout", "-B", "main"],
            check=True, capture_output=True
        )
        subprocess.run(
            ["git", "-C", repo_dir, "push", "-u", "origin", "main"],
            check=True, capture_output=True
        )
        print(f"   📤 Pushed img{repo_num} ✅")
    except Exception as e:
        print(f"   ⚠️ Push failed for img{repo_num}: {e}")

# ════════════════════════════════════════════════════════════
# تحميل الـ groups
# ════════════════════════════════════════════════════════════
def load_all_groups():
    all_groups = {}
    groups_dir = os.path.join(SCRIPT_DIR, "groups")
    if SCRIPT_DIR not in sys.path:
        sys.path.insert(0, SCRIPT_DIR)
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
# توليد البيانات المحلية
# ════════════════════════════════════════════════════════════
def generate_local_data(all_groups):
    group_name  = pick_weighted_group(all_groups)
    group       = all_groups[group_name]
    location    = random.choice(group["locations"])
    time_day    = random.choice(group["times"])
    season      = random.choice(group["seasons"])
    foreground  = random.choice(group["foregrounds"])
    mood        = random.choice(group["moods"])
    composition = random.choice(group.get("compositions", ["wide angle natural composition"]))

    base_data = {
        "group_name":  group_name,
        "location":    location,
        "time_day":    time_day,
        "season":      season,
        "foreground":  foreground,
        "mood":        mood,
        "composition": composition,
    }
    label = f"{group_name} | {location[:28]} | {season[:18]}"
    return base_data, label

# ════════════════════════════════════════════════════════════
# البروميت المحلي — بدون أسماء أماكن
# ════════════════════════════════════════════════════════════
def build_local_prompt(base_data):
    # نظّف الـ location من أسماء الأماكن
    clean_loc  = sanitize_place_names(base_data["location"])
    clean_fore = sanitize_place_names(base_data["foreground"])
    clean_mood = sanitize_place_names(base_data["mood"])

    return (
        f"{clean_loc}, {base_data['season']}. "
        f"{base_data['time_day']}. "
        f"Composition: {base_data['composition']}. "
        f"Foreground: {clean_fore}. "
        f"Mood: {clean_mood}."
    )

# ════════════════════════════════════════════════════════════
# SEO محلي — من seo_titles.py بدون أسماء أماكن
# ════════════════════════════════════════════════════════════
def build_local_seo(group_name, season, mood, keywords, gen_title_fn, get_data_fn):
    title    = gen_title_fn(group_name) if gen_title_fn else f"Natural {group_name.replace('_', ' ').title()} Landscape"
    seo_data = get_data_fn(group_name) if get_data_fn else None

    if seo_data and seo_data.get("descriptions"):
        description = random.choice(seo_data["descriptions"])
    else:
        description = f"Stunning {group_name.replace('_', ' ')} landscape. {sanitize_place_names(mood)}. Perfect for backgrounds, wallpapers, editorial, and nature projects."

    category = seo_data["category"] if seo_data else "Nature"
    core_kw  = seo_data["keywords_core"] if seo_data else []

    season_words = [w.strip() for w in season.replace(",", " ").split()[:3] if len(w) > 3]
    mood_clean   = sanitize_place_names(mood)
    mood_words   = [w.strip() for w in mood_clean.replace(",", " ").split()[:3] if len(w) > 3]

    all_keywords = list(set(
        core_kw + keywords + season_words + mood_words + [
            "nature", "landscape", "scenic", "background", "wallpaper",
            "outdoor", "natural", "wilderness", "stock photo",
            "high resolution", "horizontal", group_name.replace("_", " "),
        ]
    ))

    # نظّف الـ keywords من أسماء الأماكن
    cleaned_kw = [sanitize_place_names(kw) for kw in all_keywords]
    cleaned_kw = [kw for kw in cleaned_kw if kw.strip()]

    return {
        "title":       sanitize_place_names(title),
        "description": sanitize_place_names(description),
        "category":    category,
        "keywords":    ", ".join(cleaned_kw[:60]),
        "orientation": "Horizontal",
        "media_type":  "Photography",
    }

# ════════════════════════════════════════════════════════════
# LLM7 call
# ════════════════════════════════════════════════════════════
def call_llm7(user_message):
    response = requests.post(
        "https://api.llm7.io/v1/chat/completions",
        json={
            "model": "meta-llama/llama-3.3-70b-instruct",
            "messages": [{"role": "user", "content": user_message}],
            "max_tokens": 800,
        },
        headers={
            "Content-Type": "application/json",
            "api-key": "unused"
        },
        timeout=60
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

def parse_llm7_raw(raw):
    """يحول الـ raw output إلى dict"""
    result = {
        "prompt":      "",
        "title":       "",
        "description": "",
        "category":    "Nature",
        "keywords":    "",
    }

    current_key = None
    current_val = []

    for line in raw.split("\n"):
        clean = line.strip().replace("**", "").replace("*", "")
        if not clean:
            continue

        matched_key = None
        for key in result:
            if clean.upper().startswith(key.upper() + ":"):
                matched_key = key
                break

        if matched_key:
            if current_key and current_val:
                result[current_key] = " ".join(current_val).strip()
            current_key = matched_key
            inline = clean.split(":", 1)[1].strip()
            current_val = [inline] if inline else []
        else:
            if current_key:
                current_val.append(clean)

    if current_key and current_val:
        result[current_key] = " ".join(current_val).strip()

    return result

# ════════════════════════════════════════════════════════════
# LLM7 يولّد prompt + SEO
# 3 retries للـ API errors
# 5 retries إذا الفلتر حجب الـ output
# ════════════════════════════════════════════════════════════
def get_llm7_output(base_data, keywords):
    env_type   = base_data["group_name"].replace("_", " ")
    # نظّف الـ location من أسماء الأماكن قبل إرساله للـ AI
    loc        = sanitize_place_names(base_data["location"])[:60]
    time_day   = base_data["time_day"][:40]
    season     = base_data["season"][:40]
    foreground = sanitize_place_names(base_data["foreground"])[:40]
    mood       = sanitize_place_names(base_data["mood"])[:40]
    kw         = ", ".join(keywords[:6])

    USER = (
        f"Nature scene: {env_type}, {loc}, {time_day}, {season}, "
        f"{foreground} foreground, {mood}.\n\n"
        f"Output exactly this format:\n"
        f"PROMPT: [4 vivid sentences. Describe ONLY what is visually present: "
        f"rocks, sky, light, terrain, plants, water, clouds, sand, texture. "
        f"Write purely what you SEE. Use only positive visual descriptions. "
        f"Use ONLY general visual terms — absolutely no country names, "
        f"no city names, no mountain names, no lake names, no river names, "
        f"no region names. No specific geographic references of any kind.]\n"
        f"TITLE: [5-8 words visual description only, zero place names, zero country names]\n"
        f"DESCRIPTION: [2 sentences about visual scene and use cases, no place names]\n"
        f"CATEGORY: Nature\n"
        f"KEYWORDS: [40 comma-separated visual keywords, no place names, no country names, include: {kw}]"
    )

    filter_attempts = 0

    while filter_attempts < LLM7_FILTER_RETRIES:
        # محاولات الـ API
        raw = None
        for api_attempt in range(LLM7_API_RETRIES):
            try:
                print(f"   🤖 LLM7 generating (filter:{filter_attempts+1}/{LLM7_FILTER_RETRIES} api:{api_attempt+1}/{LLM7_API_RETRIES})...")
                raw = call_llm7(USER)
                break
            except Exception as e:
                print(f"   ⚠️ LLM7 API error (api:{api_attempt+1}/{LLM7_API_RETRIES}): {e}")
                time.sleep(5 * (api_attempt + 1))

        if not raw or len(raw) < 100:
            print(f"   ⚠️ LLM7 API failed {LLM7_API_RETRIES} times — using local fallback")
            return None

        # parsing
        result = parse_llm7_raw(raw)

        if not result["prompt"] or not result["title"] or not result["keywords"]:
            print(f"   ⚠️ LLM7 output incomplete — retrying filter attempt {filter_attempts+1}")
            filter_attempts += 1
            time.sleep(3)
            continue

        # فلتر البروميت
        ok, bad = passes_filter(result["prompt"])
        if not ok:
            print(f"   ⚠️ Filter blocked '{bad}' (filter attempt {filter_attempts+1}/{LLM7_FILTER_RETRIES})")
            filter_attempts += 1
            time.sleep(2)
            continue

        # تنظيف الـ SEO من أسماء الأماكن
        result["title"]       = sanitize_place_names(result["title"])
        result["description"] = sanitize_place_names(result["description"])
        result["keywords"]    = sanitize_place_names(result["keywords"])

        # تحقق من الـ title بعد التنظيف
        if not result["title"].strip():
            filter_attempts += 1
            continue

        print(f"   ✅ LLM7 ready ✓")
        return result

    print(f"   ⚠️ LLM7 blocked {LLM7_FILTER_RETRIES} filter attempts — using local fallback")
    return None

# ════════════════════════════════════════════════════════════
# توليد الصورة
# ════════════════════════════════════════════════════════════
def generate_image(final_prompt, output_path, prompt_source):
    full_prompt = FORCED_PREFIX + final_prompt + FORCED_SUFFIX

    # Primary: Pixazo
    try:
        print(f"   🎨 Generating with Pixazo [{prompt_source}]...")
        headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "Ocp-Apim-Subscription-Key": PIXAZO_KEY
        }
        data = {
            "prompt":    full_prompt,
            "num_steps": 8,
            "height":    1080,
            "width":     1920,
        }
        response = requests.post(
            "https://gateway.pixazo.ai/flux-1-schnell/v1/getData",
            headers=headers,
            json=data,
            timeout=60
        )
        response.raise_for_status()
        result    = response.json()
        image_url = result["output"]
        img_data  = requests.get(image_url, timeout=60).content
        with open(output_path, "wb") as f:
            f.write(img_data)
        print(f"   ✅ Saved from Pixazo")
        return "pixazo"

    except Exception as e:
        print(f"   ⚠️ Pixazo failed: {e}")
        print(f"   🔄 Switching to Pollinations FLUX.1-dev...")

    # Fallback: Pollinations
    try:
        short   = final_prompt[:250] + " Pure wilderness. Photorealistic, 8k."
        encoded = quote(short)
        url = (
            f"https://gen.pollinations.ai/image/{encoded}"
            f"?model=flux&width=1920&height=1080"
            f"&seed={random.randint(1,999999)}&nologo=true"
        )
        response = requests.get(url, timeout=120)
        response.raise_for_status()
        if len(response.content) < 10000:
            raise Exception("Image too small")
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"   ✅ Saved from Pollinations")
        return "flux-dev"

    except Exception as e:
        raise Exception(f"All image APIs failed: {e}")

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

    total_generated = get_total_generated()
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

    success      = 0
    fail         = 0
    since_push   = 0
    last_repo    = None
    modified_repos = set()

    # نستخدم while بدل for — يكمل حتى يصل للهدف
    while success < IMAGES_PER_RUN:

        repo_num, img_num, repo_dir = get_next_slot()
        if repo_num is None:
            print("✅ All repos full — done!")
            break

        print(f"\n   ── [repo{repo_num}/{img_num} | run:{success+1}/{IMAGES_PER_RUN}] ──")

        try:
            base_data, label = generate_local_data(ALL_GROUPS)
            group_name = base_data["group_name"]
            season     = base_data["season"]
            mood       = base_data["mood"]
            keywords   = ALL_GROUPS[group_name].get("stock_keywords", [])
            print(f"   📋 {label}")

            # LLM7 → 3 API retries + 5 filter retries → local fallback
            llm_output = get_llm7_output(base_data, keywords)

            if llm_output:
                final_prompt  = llm_output["prompt"]
                prompt_source = "llm7"
                is_fallback   = False
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
                # ═══ FALLBACK ═══
                print(f"   📝 Building local prompt (fallback)...")
                final_prompt  = build_local_prompt(base_data)
                prompt_source = "local"
                is_fallback   = True
                print(f"   📝 Building local SEO (fallback)...")
                seo       = build_local_seo(group_name, season, mood, keywords, GEN_TITLE, GET_SEO)
                seo_source = "seo_titles"

            # تسمية الملف — الـ fallback يأخذ "x" في النهاية
            suffix   = "x" if is_fallback else ""
            img_path = os.path.join(repo_dir, f"{img_num}{suffix}.png")
            txt_path = os.path.join(repo_dir, f"{img_num}{suffix}.txt")

            source = generate_image(final_prompt, img_path, prompt_source)

            save_txt(txt_path, seo, group_name, season, mood,
                     label, source, prompt_source, seo_source)

            success += 1
            since_push += 1
            last_repo   = repo_num
            modified_repos.add(repo_num)

            fallback_tag = " [FALLBACK ⚠️]" if is_fallback else ""
            print(f"   ✅ repo{repo_num}/{img_num}{suffix} | img:{source} | prompt:{prompt_source}{fallback_tag}")
            print(f"   📌 {seo['title'][:55]}")

            # push كل PUSH_EVERY صور
            if since_push >= PUSH_EVERY:
                push_repo(repo_num)
                since_push = 0

            time.sleep(SLEEP_BETWEEN)

        except Exception as e:
            fail += 1
            wait = random.randint(SLEEP_ON_FAIL[0], SLEEP_ON_FAIL[1])
            print(f"   ❌ Failed: {e}")
            print(f"   ⏳ Waiting {wait}s...")
            time.sleep(wait)
            # لا يزيد success → يحاول مرة أخرى تلقائياً

    # final push لكل الـ repos المعدّلة
    print(f"\n   📤 Final push for modified repos...")
    for repo_num in modified_repos:
        push_repo(repo_num)

    final_total = get_total_generated()
    print("\n" + "=" * 60)
    print(f"✅ Run complete!")
    print(f"   This run: {success} ✅ | {fail} ❌")
    print(f"   Total generated: {final_total} / {total_capacity}")
    print(f"   Remaining: {total_capacity - final_total}")
    print("=" * 60)
