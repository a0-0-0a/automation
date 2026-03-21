COMPOSITIONS_OCEAN = [
    "wide angle, rocky foreground, sea and horizon beyond",
    "cliff edge view, sea far below, horizon far beyond",
    "looking along coastline, cliffs receding into distance",
    "low angle on rocks, waves and open sea beyond",
    "aerial view looking down at coast and sea from above",
    "beach close foreground, sea middle distance, horizon far",
    "rock pool in foreground, sea and cliffs beyond",
    "cliff top view looking straight down at sea below",
]

DAYTIME = [
    "bright clear midmorning, vivid deep blue sea, sharp crisp shadows",
    "brilliant sunny midday, deep blue ocean, vivid coastal colors",
    "perfect clear afternoon, maximum ocean color saturation, vivid",
    "clear sunny morning, vivid blue coastal colors, bright clean light",
]
GOLDEN = [
    "golden hour sunset, warm light on waves, long vivid reflections",
    "magic hour sunrise, pink sky perfectly reflected on calm sea",
    "late afternoon golden light glowing on coastal cliffs and rocks",
]
ALL_TIMES = DAYTIME + GOLDEN

GROUPS = {
    "dramatic_sea_cliffs": {
        "locations": [
            "Faroe Islands, sheer dramatic green cliffs above Atlantic ocean",
            "Big Sur California, dramatic rocky Pacific coastline cliffs",
            "Wild Atlantic Way Ireland, jagged raw Atlantic rocky coastline",
            "Moher Cliffs Ireland, sheer limestone above green Atlantic",
            "Cape Breton Nova Scotia, dramatic high cliff coastline",
            "Azores volcanic cliffs, dark black rock above Atlantic ocean",
            "Etretat France, white chalk cliffs above deep blue sea",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_OCEAN,
        "seasons": [
            "summer, deep vivid blue sea, clear bright sky",
            "spring, clear fresh light, vivid natural colors",
            "autumn, dramatic vivid sky, clear sea visibility",
            "winter clear day, cold crisp blue light, deep blue water",
        ],
        "foregrounds": [
            "rough barnacle-covered coastal rock, natural organic texture",
            "jagged cliff edge with natural varied lichen coverage",
            "coastal rock close-up, barnacles and natural surface texture",
            "rough wet dark rock surface, natural coastal detail",
            "tide pool in foreground, clear water, sea beyond",
        ],
        "moods": [
            "raw ocean power, dramatic natural coastal force",
            "vivid deep blue ocean, brilliant natural coastal clarity",
            "dramatic ancient geological coastline, timeless rock and sea",
            "fresh sea air, crisp clear natural coastal light",
        ],
        "stock_keywords": [
            "ocean", "sea cliffs", "coast", "Atlantic", "coastal", "dramatic",
            "marine", "seascape", "rocky", "waves", "shore", "cliffs", "nature"
        ],
    },
    "beach_seascape": {
        "locations": [
            "Iceland Reynisfjara, black volcanic sand beach basalt columns",
            "Calanques France, white limestone cliffs above vivid turquoise water",
            "Sardinia Costa Smeralda, vivid turquoise sea white rocky beach",
            "Lofoten Norway, jagged dramatic peaks above dark cold sea",
            "New Zealand Abel Tasman, golden sand vivid clear water",
            "Greece Santorini caldera, deep vivid blue sea dramatic view",
            "Croatia Dalmatian coast, vivid turquoise sea rocky shore",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_OCEAN,
        "seasons": [
            "summer, deep vivid blue sea, clear bright sky",
            "spring, clear fresh light, vivid natural sea colors",
            "autumn, dramatic sky, clear vivid sea",
            "winter clear day, cold crisp light, deep blue water",
        ],
        "foregrounds": [
            "coarse black volcanic sand with wave-smoothed natural stones",
            "smooth rounded boulders with natural kelp and seaweed",
            "wet sand with natural foam patterns at wave retreat",
            "rounded pebbles on shoreline, varied natural colors sizes",
            "clear shallow water over natural rocky bottom, vivid",
        ],
        "moods": [
            "serene clear sea, peaceful bright natural reflection",
            "dramatic natural waves, raw coastal power",
            "vivid blue water, brilliant natural coastal beauty",
            "peaceful empty natural beach, pure natural solitude",
        ],
        "stock_keywords": [
            "beach", "ocean", "sea", "coastal", "waves", "shore", "marine",
            "turquoise", "water", "sand", "seascape", "coast", "nature"
        ],
    },
}
