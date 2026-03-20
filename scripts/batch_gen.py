import os
import random
import time
import requests
import subprocess

# ════════════════════════════════════════════════════════════
# إعدادات
# ════════════════════════════════════════════════════════════
PIXAZO_KEY      = os.environ.get("PIXAZO_KEY", "")
BASE_DIR        = "imgs"
IMAGES_PER_REPO = 1000
TOTAL_REPOS     = 10
TOTAL_TARGET    = IMAGES_PER_REPO * TOTAL_REPOS  # 10,000
SLEEP_BETWEEN   = 5
SLEEP_ON_FAIL   = (30, 60)
PUSH_EVERY      = 50

FORCED_PREFIX = (
    "Pure nature landscape only, zero humans, zero people, zero faces, "
    "zero animals, zero insects, zero birds, zero living creatures, "
    "zero man-made objects, zero buildings, zero roads, zero vehicles. "
    "Vast empty untouched wilderness only. "
)

DAYTIME_HEAVY = [
    "bright clear midmorning, direct warm sun, sharp crisp shadows",
    "brilliant sunny midday, intense overhead sun, vivid saturated colors",
    "clear bright morning, fresh warm light, defined shadows everywhere",
    "sunny late morning, warm directional light, rich color saturation",
    "perfect clear afternoon, bright warm sun, sharp long shadows",
    "bright clear midday, cloudless sky, maximum color and clarity",
    "warm clear morning light, sun well above horizon, vivid tones",
    "brilliant clear afternoon, direct sunlight, crisp sharp shadows",
    "clear sunny midmorning, vivid colors, bright natural light",
    "perfect blue sky midday, intense sun, deep shadow contrast",
    "clear bright late morning, warm sun, rich vivid colors",
    "sunny clear afternoon, strong directional light, sharp shadows",
]

GOLDEN_TIMES = [
    "golden hour 45 minutes before sunset, long warm orange shadows",
    "magic hour sunrise, pink gold sky, warm front light",
    "late afternoon golden light, warm side illumination, long shadows",
    "early morning golden light, warm raking light, vivid colors",
]

ALL_TIMES = DAYTIME_HEAVY + GOLDEN_TIMES

GROUPS = {

    "hot_desert": {
        "locations": [
            "Saharan desert Algeria, massive asymmetric orange sand dunes",
            "Rub al Khali Saudi Arabia, endless red star dunes",
            "Atacama desert Chile, pale cracked salt formations and strange rocks",
            "Wadi Rum Jordan, massive red sandstone canyon formations",
            "Namib desert Namibia, tall ancient red dunes",
            "Sahara desert Morocco, golden sand sea stretching to horizon",
            "Arabian desert Oman, pristine untouched golden dunes",
            "Sonoran desert Arizona, rocky terrain with massive boulders",
            "Dasht-e Kavir Iran, vast white salt flat desert",
            "Sahara desert Libya, perfect undisturbed sand dune field",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "peak summer, extreme heat, bleached pale blue sky",
            "winter desert, cool clear crisp air, vivid warm colors",
            "after rare desert rain, dark wet sand, dramatic contrast",
            "desert bloom, rare scattered wildflowers between rocks",
            "spring, perfect clear light, rich warm tones",
            "dry season, maximum color saturation, crystal clear air",
        ],
        "foregrounds": [
            "rippled sand surface, wind patterns, varying depth and spacing",
            "rough sandstone rock fragments, sharp edges, varied warm colors",
            "dried salt crust on flat ground, crystalline white surface",
            "coarse desert gravel, small smooth pebbles, red-orange tones",
            "wind-sculpted sand ripples close-up, precise natural patterns",
            "large flat sandstone slabs, warm tones, sharp shadows",
            "smooth desert pebbles of varied size and warm color",
            "fine orange sand with small dark pebbles scattered",
        ],
        "moods": [
            "vast solitude, timeless heat, ancient geological silence",
            "dramatic epic scale, raw power of desert landscape",
            "peaceful golden warmth, serene emptiness",
            "stark minimalist beauty, pure elemental forms",
            "rich warm tones, saturated golden desert atmosphere",
        ],
    },

    "arctic_tundra": {
        "locations": [
            "Arctic tundra Svalbard, frozen ground with low vegetation",
            "Greenland ice sheet, endless white surface to horizon",
            "Icelandic highland interior, snow-covered volcanic plateau",
            "Canadian arctic tundra, snow-covered ground and frozen lake",
            "Norwegian arctic coastline, frozen ground and pale blue sky",
            "Alaska North Slope, flat frozen tundra, low horizon",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "deep polar winter, complete snow cover, pale cold blue sky",
            "brief arctic summer, low clear sun, tundra grasses visible",
            "arctic spring, patches of dark earth through melting snow",
            "clear cold autumn, first frost on tundra ground",
            "bright winter day, brilliant white snow, clear blue sky",
        ],
        "foregrounds": [
            "fresh powder snow surface with subtle blue shadow variations",
            "windblown snow surface with fine rippled patterns",
            "frost-covered low vegetation stubble on frozen tundra ground",
            "dark rock partially exposed through surrounding snow",
            "flat snow surface with natural light and shadow texture",
            "snow crystals on frozen ground surface, fine detail",
        ],
        "moods": [
            "extreme cold silence, pristine frozen world",
            "austere stark beauty, white and blue minimal palette",
            "crisp perfect clarity, clean frozen air",
            "brilliant white landscape, pure light and shadow",
            "vast open frozen space, endless horizon",
        ],
    },

    "tropical_rainforest": {
        "locations": [
            "Amazon rainforest canopy Brazil, dense uneven treetops from above",
            "Borneo rainforest Sabah, ancient towering emergent trees",
            "Congo basin forest, dense humid forest interior",
            "Daintree rainforest Australia, ancient tropical forest floor",
            "Sumatra lowland rainforest, massive ancient dipterocarp trees",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "peak wet season, dripping surfaces, deep saturated greens",
            "dry season, clear light, rich vivid green tones",
            "after heavy tropical rain, vivid glistening surfaces",
            "peak growth season, lush dense vegetation, vivid colors",
        ],
        "foregrounds": [
            "massive exposed tree trunks on dark humid forest floor",
            "dense carpet of ferns on irregular rocky ground",
            "large tropical leaves of varied shape and size overlapping",
            "dark rich forest soil with small plants and leaf litter",
            "shallow clear forest stream flowing over mossy rocks",
            "vivid green moss covering large boulders on forest floor",
        ],
        "moods": [
            "ancient primordial, untouched for millions of years",
            "dense humid abundance, overwhelming green complexity",
            "alive with growth, constant natural richness",
            "cool shaded interior, golden light filtering through canopy",
            "sacred old growth, ancient beyond measure",
        ],
    },

    "temperate_forest": {
        "locations": [
            "Muir Woods redwood forest California, towering trunks dark floor",
            "Yakushima cedar forest Japan, ancient mossy trees",
            "Olympic rainforest Washington, moss-draped temperate forest",
            "Białowieża primeval forest Poland, ancient mixed forest",
            "Appalachian forest eastern USA, dense deciduous forest",
            "Black Forest Germany, dense dark spruce forest",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "peak autumn, saturated orange gold red leaves, fallen leaf carpet",
            "deep winter, snow on branches, sharp shadows on snow",
            "early spring, pale fresh green buds on dark branches",
            "peak summer, full dense green canopy, filtered light",
            "spring wildflowers carpet on bright forest floor",
            "late summer, rich deep green canopy, warm golden tones",
        ],
        "foregrounds": [
            "fallen autumn leaves in various colors and stages of decay",
            "dense moss covering irregular rocks and ground",
            "forest floor ferns of varied height and density",
            "scattered pinecones and needles on dark rich soil",
            "bright wildflowers scattered on forest floor",
            "autumn leaf carpet, varied colors, natural disorder",
        ],
        "moods": [
            "peaceful quiet forest, warm natural light",
            "ancient old growth, centuries of undisturbed growth",
            "seasonal richness, vivid autumn or spring colors",
            "sheltered warmth, forest filled with golden light",
            "rich layered forest, complex natural beauty",
        ],
    },

    "alpine_mountain": {
        "locations": [
            "Swiss Alps Lauterbrunnen, vertical cliffs with hanging waterfalls",
            "Dolomites South Tyrol, pale vertical limestone towers",
            "Patagonia Torres del Paine, jagged granite peaks",
            "Rockies Banff, vivid turquoise lake surrounded by forested peaks",
            "New Zealand Southern Alps, snow peaks above green valleys",
            "Alps Austria, steep green slopes with rocky peaks above",
            "Himalayas Nepal, massive snow peaks rising above clouds",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "peak summer, green lower slopes, snow on high peaks",
            "deep winter, everything snow-covered, brilliant white peaks",
            "peak autumn, golden forest in valley, snow on high peaks",
            "spring, fresh green emerging, snow still on high peaks",
            "clear summer, deep blue sky, vivid green and white",
        ],
        "foregrounds": [
            "rough alpine rock surface with varied lichen coverage",
            "alpine wildflowers scattered between rocks, vivid colors",
            "coarse mountain gravel and broken rock fragments",
            "high altitude sparse grass between rocky outcrops",
            "close wildflower bloom on rocky alpine ground",
            "snow-dusted rocky ground with exposed stones",
        ],
        "moods": [
            "epic scale, mountains dwarfing everything below",
            "crisp thin mountain air, perfect crystal clarity",
            "peaceful solitude, remote high altitude beauty",
            "brilliant clear mountain day, vivid saturated colors",
            "dramatic power, raw geological force",
        ],
    },

    "ocean_coast": {
        "locations": [
            "Faroe Islands sea cliffs, sheer green cliffs above Atlantic",
            "Big Sur California, dramatic rocky coastline Pacific",
            "Lofoten islands Norway, jagged peaks rising from dark sea",
            "Calanques coast France, white limestone cliffs above turquoise water",
            "Iceland black sand beach Reynisfjara, basalt columns and waves",
            "Wild Atlantic Way Ireland, jagged rocky Atlantic coastline",
            "Azores ocean cliffs, volcanic black rock above Atlantic",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "summer calm, deep vivid blue sea, clear sky",
            "spring, clear fresh light, vivid colors",
            "autumn, dramatic sky, clear visibility, vivid sea",
            "winter clear day, cold crisp light, deep blue water",
        ],
        "foregrounds": [
            "rough wet barnacle-covered rock with tide pools",
            "coarse black volcanic sand with wave-smoothed stones",
            "jagged sea cliff edge covered in lichen",
            "smooth boulders with kelp and seaweed",
            "wet sand with foam patterns at wave retreat",
            "coastal rock close-up with barnacles and natural texture",
        ],
        "moods": [
            "raw ocean power, constant dramatic movement",
            "serene clear sea, peaceful bright reflection",
            "vivid blue open ocean, brilliant coastal clarity",
            "fresh sea air, crisp bright coastal light",
            "dramatic coastal geology, ancient rock and sea",
        ],
    },

    "canyon_rock_formation": {
        "locations": [
            "Grand Canyon inner gorge Arizona, layered red and brown walls",
            "Antelope Canyon Arizona, smooth curved orange sandstone walls",
            "Bryce Canyon Utah, dense orange hoodoo rock spires",
            "Canyonlands Utah, vast layered red rock plateau and canyons",
            "Cappadocia valley Turkey, eroded soft volcanic rock formations",
            "Wave formation Arizona, smooth curved layered sandstone",
            "Quebrada Humahuaca Argentina, vivid layered colored cliffs",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "summer, dry clear air, vivid saturated rock colors",
            "winter, light dusting of snow on red rock ledges, clear sky",
            "spring, crystal clear light, maximum color saturation",
            "autumn, perfect clear light, warm rich deep tones",
        ],
        "foregrounds": [
            "layered sandstone surface with varied texture and color bands",
            "rough broken rock fragments at canyon base",
            "fine red sand on canyon floor with ripple patterns",
            "cross-bedded sandstone detail showing diagonal layering",
            "smooth curved sandstone wall with warm color gradient",
            "large flat rock slabs, warm orange tones, sharp shadows",
        ],
        "moods": [
            "geological time made visible, ancient layered rock",
            "warm saturated color, rich deep rock tones",
            "dramatic light and shadow, sharp contrast beauty",
            "vivid warm palette, rich orange and red tones",
            "ancient erosion, water carved over millennia",
        ],
    },

    "river_lake_wetland": {
        "locations": [
            "Plitvice lakes Croatia, cascading turquoise terraced pools",
            "Lake Baikal Russia, clear deep blue lake surface",
            "Norwegian fjord Geiranger, dark water and vertical cliffs",
            "New Zealand fiordland, mirror-still dark fjord water",
            "Patagonia glacial lake, vivid turquoise milky water",
            "Iceland glacial river, braided channels across flat plain",
            "Banff Lake Louise, vivid turquoise glacial lake",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "summer, clear vivid water, maximum color",
            "autumn, golden reflections in perfectly still water",
            "spring, fresh clear light, clean high water",
            "winter clear day, thin ice forming at edges, crisp light",
        ],
        "foregrounds": [
            "smooth water-worn stones on shoreline, varied sizes",
            "river gravel bar, fine to coarse sorted stones",
            "clear shallow water over detailed rocky bottom",
            "wet rocks at waterline, varied texture and color",
            "shallow clear pool with rocks visible through water",
            "pebbles and stones at water edge, wet and dry contrast",
        ],
        "moods": [
            "perfectly still, glassy reflection, profound calm",
            "vivid turquoise color, rich and clear water",
            "cool fresh water atmosphere, clean perfect clarity",
            "peaceful lakeside calm, clear natural reflections",
            "flowing movement, bright water in motion",
        ],
    },

    "grassland_savanna": {
        "locations": [
            "Mongolian steppe Gobi, endless rolling golden grassland",
            "Patagonian steppe Argentina, windswept golden grass plains",
            "Kansas tallgrass prairie USA, rolling sea of grass",
            "New Zealand tussock grassland, golden tussock slopes",
            "Tibetan plateau Qinghai, high altitude grass plateau",
            "Kazakh steppe, flat endless grass stretching to horizon",
            "South African highveld, open golden grass plateau",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "peak summer, tall golden dry grass, bright clear sky",
            "spring, fresh short vivid green grass",
            "autumn, tawny brown dried grass, clear cold light",
            "early summer, mixed green and gold, rich warm tones",
            "late summer, deep golden grass, vivid warm light",
        ],
        "foregrounds": [
            "close grass stems of varied height in gentle wind",
            "dried grass seed heads close-up, fine natural detail",
            "mixed grass species of varied heights and textures",
            "windswept flattened grass showing wind direction",
            "grass close-up, warm backlit golden tones",
            "tussock grass clumps, varied rounded organic shapes",
        ],
        "moods": [
            "vast open endless, sky and grass only",
            "golden warmth, peaceful open plain",
            "windswept solitude, constant grass movement",
            "rich golden light, warm grassland atmosphere",
            "elemental simplicity, pure horizontal golden space",
        ],
    },

    "macro_closeup_nature": {
        "locations": [
            "single wildflower bloom, soft blurred natural background",
            "fern frond close-up, soft green background",
            "single flower petal close-up, shallow depth of field",
            "moss close-up, tiny intricate green structures",
            "lichen on rock surface close-up, abstract texture",
            "grass seed head close-up, soft bokeh background",
            "single autumn leaf close-up, blurred forest floor",
            "tree bark texture close-up, detailed wood grain",
            "stone surface close-up, mineral patterns and texture",
            "pine cone scale detail, natural geometric pattern",
            "flower stamen close-up, abstract natural beauty",
            "pebble collection close-up, varied colors and textures",
            "dewdrop on leaf surface, macro detail",
            "seedpod close-up, intricate natural structure",
        ],
        "times": ALL_TIMES,
        "seasons": [
            "spring bloom, fresh vivid color, new growth",
            "summer, rich saturated color, full bloom",
            "autumn, warm gold tones, changing color",
            "peak flower season, maximum vivid color",
            "early spring, delicate fresh colors",
        ],
        "foregrounds": [
            "subject perfectly sharp, everything else soft blur",
            "extreme close focus, full frame natural detail",
            "shallow depth of field, sharp center, soft edges",
            "macro detail, tiny natural structures revealed",
            "intimate close view, natural texture fills frame",
        ],
        "moods": [
            "intimate and delicate, quiet natural beauty",
            "vivid fresh color, nature at its most beautiful",
            "serene natural detail, meditative close focus",
            "soft warm light on natural subject, gentle mood",
            "peaceful close observation, calm and still",
        ],
    },

}

# ════════════════════════════════════════════════════════════
# حساب الصور الموجودة
# ════════════════════════════════════════════════════════════
def count_images_in_repo(repo_index):
    repo_dir = os.path.join(BASE_DIR, f"img{repo_index}")
    if not os.path.exists(repo_dir):
        return 0
    return len([
        f for f in os.listdir(repo_dir)
        if f.endswith(".png") and f[:-4].isdigit()
    ])

def get_next_number():
    all_existing = []
    for i in range(1, TOTAL_REPOS + 1):
        repo_dir = os.path.join(BASE_DIR, f"img{i}")
        if os.path.exists(repo_dir):
            existing = [
                int(f[:-4]) for f in os.listdir(repo_dir)
                if f.endswith(".png") and f[:-4].isdigit()
            ]
            all_existing.extend(existing)
    if not all_existing:
        return 1
    return max(all_existing) + 1

def get_repo_dir(num):
    repo_index = ((num - 1) // IMAGES_PER_REPO) + 1
    repo_index = min(repo_index, TOTAL_REPOS)
    repo_dir   = os.path.join(BASE_DIR, f"img{repo_index}")
    os.makedirs(repo_dir, exist_ok=True)
    return repo_dir, repo_index

def all_repos_full():
    for i in range(1, TOTAL_REPOS + 1):
        if count_images_in_repo(i) < IMAGES_PER_REPO:
            return False
    return True

# ════════════════════════════════════════════════════════════
# Push للـ repos
# ════════════════════════════════════════════════════════════
def push_all_repos():
    print("\n   🔄 جاري الـ push...")
    for i in range(1, TOTAL_REPOS + 1):
        repo_dir = os.path.join(BASE_DIR, f"img{i}")
        if not os.path.exists(repo_dir):
            continue
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo_dir,
            capture_output=True, text=True
        )
        if result.stdout.strip():
            subprocess.run(["git", "add", "."], cwd=repo_dir)
            subprocess.run(["git", "commit", "-m", "add images batch"], cwd=repo_dir)
            subprocess.run(["git", "push"], cwd=repo_dir)
            print(f"   ✅ pushed img{i}")

# ════════════════════════════════════════════════════════════
# توليد البروميت
# ════════════════════════════════════════════════════════════
def generate_prompt():
    group_name = random.choice(list(GROUPS.keys()))
    group      = GROUPS[group_name]
    location   = random.choice(group["locations"])
    time_day   = random.choice(group["times"])
    season     = random.choice(group["seasons"])
    foreground = random.choice(group["foregrounds"])
    mood       = random.choice(group["moods"])

    prompt = (
        f"{FORCED_PREFIX}"
        f"{location}, {season}. "
        f"{time_day}. "
        f"Foreground detail: {foreground}. "
        f"Atmosphere: {mood}. "
        f"Natural imperfections throughout, no repeated patterns, "
        f"no uniform elements, organic irregular shapes only. "
        f"Shot on Hasselblad H6D, RAW format, photorealistic, "
        f"real location on Earth, 8k ultra detailed, "
        f"National Geographic cover shot, no humans, no animals, "
        f"no man-made objects, no repeated patterns."
    )
    label = f"{group_name} | {location[:25]} | {season[:15]}"
    return prompt, label

# ════════════════════════════════════════════════════════════
# توليد الصورة
# ════════════════════════════════════════════════════════════
def generate_image(prompt, output_path):
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Ocp-Apim-Subscription-Key": PIXAZO_KEY
    }
    data = {
        "prompt": prompt,
        "num_steps": 8,
        "height": 1344,
        "width": 768,
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

# ════════════════════════════════════════════════════════════
# الـ BATCH LOOP
# ════════════════════════════════════════════════════════════
if __name__ == "__main__":

    # تحقق إذا كل الـ repos ممتلئة
    if all_repos_full():
        print("✅ كل الـ repos ممتلئة! (10,000 صورة)")
        exit(0)

    start_from = get_next_number()

    print("=" * 60)
    print(f"  Batch Image Generator — GitHub Actions")
    print(f"  البداية من      : {start_from}")
    print(f"  الهدف           : {TOTAL_TARGET}")
    print(f"  المتبقي         : {TOTAL_TARGET - start_from + 1}")
    print(f"  البيئات         : {len(GROUPS)} groups")
    print(f"  push كل         : {PUSH_EVERY} صورة")
    for i in range(1, TOTAL_REPOS + 1):
        count = count_images_in_repo(i)
        print(f"  img{i:<3}          : {count}/{IMAGES_PER_REPO}")
    print("=" * 60)

    success = 0
    fail    = 0
    num     = start_from

    while num <= TOTAL_TARGET:

        # تحقق إذا كل الـ repos ممتلئة
        if all_repos_full():
            print("\n✅ كل الـ repos ممتلئة! 10,000 صورة اكتملت!")
            push_all_repos()
            break

        repo_dir, repo_index = get_repo_dir(num)

        # تحقق إذا هذا الـ repo ممتلئ
        if count_images_in_repo(repo_index) >= IMAGES_PER_REPO:
            num = (repo_index * IMAGES_PER_REPO) + 1
            continue

        output_path = os.path.join(repo_dir, f"{num}.png")

        if os.path.exists(output_path):
            print(f"   [{num}/{TOTAL_TARGET}] موجود مسبقاً — تخطي")
            num += 1
            continue

        try:
            prompt, label = generate_prompt()
            generate_image(prompt, output_path)

            success += 1
            print(f"   [{num}/{TOTAL_TARGET}] ✅ | {label}")
            num += 1
            time.sleep(SLEEP_BETWEEN)

        except Exception as e:
            fail += 1
            wait = random.randint(SLEEP_ON_FAIL[0], SLEEP_ON_FAIL[1])
            print(f"   [{num}/{TOTAL_TARGET}] ⚠️ فشل: {e}")
            print(f"   انتظار {wait} ثانية...")
            time.sleep(wait)

        # push كل PUSH_EVERY صورة
        if success > 0 and success % PUSH_EVERY == 0:
            push_all_repos()

    # push نهائي
    push_all_repos()

    print("\n" + "=" * 60)
    print(f"✅ انتهى الـ run!")
    print(f"   نجح  : {success}")
    print(f"   فشل  : {fail}")
    print("=" * 60)
