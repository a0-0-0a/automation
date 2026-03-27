COMPOSITIONS_FOREST = [
    "looking down a forest path between tall trunks, perspective lines",
    "wide angle low angle, massive trunks rising above, canopy above",
    "forest floor close, trunks middle distance, canopy far above",
    "sidelit forest, light coming from one side through trunks",
    "looking up at canopy from below, trunks radiating outward",
    "forest edge, open bright area visible through trees",
    "dense forest interior, shafts of light hitting forest floor",
    "forest path curves ahead, trees on both sides",
]

DAYTIME = [
    "bright clear midmorning, strong direct sunlight through canopy, bright floor fully visible",
    "bright midday, strong sunlight shafts, forest floor clearly illuminated throughout",
    "clear sunny afternoon, strong warm light fully penetrating canopy, bright visible",
    "golden hour strong warm shafts through forest trunks, floor brightly lit",
    "bright clear morning, direct sunlight filtering through, well-lit forest",
]
ALL_TIMES = DAYTIME

GROUPS = {
    "temperate_forest": {
        "locations": [
            "towering ancient redwood trunks bright",
            "ancient massive oak trees",
            "moss-draped trees bright floor",
            "dense ancient deciduous forest bright",
            "dense spruce dramatic bright light shafts",
            "old-growth temperate rainforest bright floor",
            "ancient mixed forest bright light",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_FOREST,
        "seasons": [
            # ✅ temperate forests DO have all 4 seasons
            "peak autumn, saturated orange gold red leaves, bright fallen leaf carpet",
            "early spring, pale fresh green new buds, bright warm light on branches",
            "peak summer, rich green canopy, strong bright shafts of light",
            "deep winter, snow on branches, bright light and blue-white shadows on snow",
        ],
        "foregrounds": [
            "fallen autumn leaves, varied colors, natural organic disorder, bright",
            "bright dense moss covering irregular rocks and floor",
            "bright forest floor ferns of varied natural height",
            "scattered bright leaves and forest debris on well-lit soil",
            "bright small wildflowers on bright forest floor",
        ],
        "moods": [
            "bright ancient forest, cathedral golden light fully illuminated",
            "warm bright peaceful shelter, strong golden filtered light",
            "seasonal richness, vivid bright natural autumn or spring color",
            "bright mysterious depth, strong light fully piercing forest",
        ],
        "stock_keywords": [
            "forest", "woodland", "trees", "ancient", "nature", "green",
            "autumn", "woods", "canopy", "sunbeam", "light", "serene", "bright"
        ],
    },
    "tropical_forest": {
        "locations": [
            "dense uneven treetops from above",
            "ancient towering emergent trees bright",
            "ancient tropical bright forest",
            "dense humid forest bright interior",
            "massive ancient trees bright shafts",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_FOREST,
        "seasons": [
            # ✅ tropical forests only have wet/dry seasons — NO winter, NO spring buds
            "peak wet season, dripping surfaces, deep bright saturated vivid greens",
            "dry season, bright clear light, rich vivid deep green tones",
            "after heavy tropical rain, vivid bright glistening wet surfaces",
            "peak growth season, lush dense vivid vegetation, bright colors",
        ],
        "foregrounds": [
            "massive ancient exposed tree trunks on bright humid floor",
            "dense carpet of ferns on bright irregular rocky ground",
            "large tropical leaves varied shape size, bright and vivid",
            "dark rich soil with bright small varied tropical plants",
            "vivid bright green moss covering large irregular boulders",
        ],
        "moods": [
            "ancient primordial, bright and untouched for millions of years",
            "dense humid abundance, bright overwhelming green complexity",
            "bright cool shaded interior, strong golden light filtering through canopy",
            "alive with constant bright natural growth, vivid natural richness",
        ],
        "stock_keywords": [
            "rainforest", "tropical", "jungle", "green", "canopy", "nature",
            "lush", "forest", "humid", "ancient", "bright"
        ],
    },
}
