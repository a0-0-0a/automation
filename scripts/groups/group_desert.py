COMPOSITIONS_DESERT = [
    "wide angle, sand foreground, dunes receding to horizon",
    "looking along dune ridge, perspective lines receding",
    "dune face filling frame, texture and shadow detail",
    "aerial view looking down at dune patterns from above",
    "low angle on sand surface, dunes rising dramatically above",
    "salt flat perspective, cracked patterns receding to horizon",
]

DAYTIME = [
    "bright clear midmorning, direct warm sun, sharp crisp shadows on sand",
    "brilliant sunny midday, intense overhead sun, vivid saturated desert colors",
    "perfect clear afternoon, warm sun, long sharp shadows across dunes",
    "warm clear morning, sun well above horizon, vivid warm sand tones",
    "clear sunny midmorning, vivid golden colors, bright crisp light",
]
GOLDEN = [
    "golden hour 45 minutes before sunset, long orange shadows on dunes",
    "magic hour sunrise, pink gold sky, warm raking light across sand",
    "late afternoon golden light, warm side light on dune faces",
]
ALL_TIMES = DAYTIME + GOLDEN

GROUPS = {
    "saharan_dunes": {
        "locations": [
            "massive asymmetric orange sand dunes",
            "endless deep red star dunes",
            "golden sand sea stretching to horizon",
            "pristine untouched golden dunes",
            "perfect undisturbed sand dune field",
            "classic tall orange desert dunes",
            "massive smooth red sand dunes",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_DESERT,
        "seasons": [
            "peak summer, extreme heat, bleached pale blue sky",
            "winter desert, cool clear crisp air, vivid warm sand colors",
            "spring, perfect clear light, rich warm golden tones",
            "dry season, maximum color saturation, crystal clear air",
        ],
        "foregrounds": [
            "rippled sand surface, precise wind patterns, natural spacing",
            "wind-sculpted sand ripples close-up, perfect natural geometry",
            "smooth sand with small dark pebbles scattered naturally",
            "fine orange sand texture, subtle natural color gradients",
            "sand ripple patterns leading naturally to distant dune",
        ],
        "moods": [
            "vast solitude, timeless heat, ancient geological silence",
            "peaceful golden warmth, serene pure emptiness",
            "stark minimalist beauty, pure natural forms",
            "rich warm tones, saturated golden desert atmosphere",
        ],
        "stock_keywords": [
            "desert", "sand dunes", "arid", "golden", "landscape",
            "nature", "scenic", "background", "wallpaper", "warm", "minimal"
        ],
    },
    "rocky_desert": {
        "locations": [
            "massive red sandstone canyon formations",
            "pale cracked salt and strange rock formations",
            "rocky terrain with massive rounded boulders",
            "vast white salt flat with distant mountains",
            "cracked salt pan with geometric patterns",
            "pure white gypsum dune field",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_DESERT,
        "seasons": [
            "dry season, vivid saturated rock colors, crystal clear air",
            "winter desert, cool clear light, vivid warm rock colors",
            "spring, perfect clear light, maximum color saturation",
            "after rare desert rain, dark wet rock surface, dramatic contrast",
        ],
        "foregrounds": [
            "rough sandstone rock fragments, sharp edges, warm varied colors",
            "dried salt crust on flat ground, white crystalline surface",
            "coarse desert gravel, smooth pebbles, red-orange natural tones",
            "cracked dry earth, natural polygon patterns, warm tones",
            "flat sandstone slabs, warm tones, sharp natural shadows",
        ],
        "moods": [
            "dramatic epic scale, raw geological power",
            "ancient geological time, raw rock formations",
            "warm saturated color, rich desert rock tones",
            "remote untouched, pure geological beauty",
        ],
        "stock_keywords": [
            "desert", "rock", "canyon", "arid", "geology", "landscape",
            "red rock", "sandstone", "nature", "scenic", "dry"
        ],
    },
}
