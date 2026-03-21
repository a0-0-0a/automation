COMPOSITIONS_MOUNTAIN = [
    "wide angle view, detailed rocky foreground, mountains filling background",
    "telephoto compressed view, multiple mountain layers stacked behind each other",
    "aerial view looking down at mountain valley and ridgelines from above",
    "looking up from deep valley floor, towering peaks on both sides",
    "mountain peaks emerging naturally above low real morning cloud layer",
    "dramatic ridgeline silhouette against bright clear sky, sharp jagged peaks",
    "diagonal mountain face filling frame, natural rock layers and texture",
    "panoramic view of entire mountain range, horizon to horizon",
    "close view of snow-covered mountain slope, natural snow texture detail",
    "mountain valley between two peaks, visible below",
    "mountain base view, massive rock wall rising vertically from ground",
    "mountain glacier close view, ice texture and crevasses detail",
]

DAYTIME = [
    "bright clear midmorning, direct sun on rock faces, sharp natural shadows",
    "brilliant sunny midday, vivid mountain colors, crisp clear real air",
    "perfect clear afternoon, warm light on peaks, sharp natural shadows",
    "clear sunny morning, vivid mountain colors, bright crisp real light",
    "perfect natural blue sky midday, deep natural blue, brilliant white snow",
]
GOLDEN = [
    "alpine glow, peaks turning natural pink red at last real golden light",
    "golden hour, natural warm light on rocky faces, long real mountain shadows",
    "magic hour sunrise, natural pink gold sky, warm light on highest peaks",
    "early morning golden light, first warm natural rays on real snow peaks",
]
ALL_TIMES = DAYTIME + GOLDEN

GROUPS = {
    "limestone_peaks": {
        "locations": [
            "Dolomites South Tyrol Italy, pale vertical limestone towers",
            "Swiss Alps Lauterbrunnen, vertical cliffs with hanging waterfalls",
            "Dolomites Tre Cime Italy, three vertical rock towers blue sky",
            "Alps Austria, steep green slopes with pale rocky peaks above",
            "Dolomites Seceda Italy, dramatic ridgeline against vivid blue sky",
            "Dolomites Cinque Torri Italy, five rock towers on open plateau",
            "Swiss Alps Eiger, massive north face sheer vertical wall",
            "Dolomites Marmolada Italy, highest peak with massive glacier",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_MOUNTAIN,
        "seasons": [
            "peak summer, vivid green lower slopes, brilliant white snow peaks",
            "deep winter, everything snow-covered, pure white peaks blue sky",
            "peak autumn, golden forest in valley, snow on high peaks",
            "spring, fresh green emerging below, snow still on high peaks",
        ],
        "foregrounds": [
            "rough alpine rock surface with varied natural lichen coverage",
            "alpine wildflowers scattered between rocks, vivid small blooms",
            "coarse mountain gravel and natural broken rock fragments",
            "high altitude sparse grass between irregular rocky outcrops",
            "snow-dusted rocky ground with exposed natural stones",
            "close view of mountain rock texture and mineral detail",
        ],
        "moods": [
            "epic massive real scale, mountains dwarfing everything below",
            "crisp thin real mountain air, perfect crystal natural clarity",
            "peaceful high altitude real solitude, remote natural beauty",
            "brilliant clear real mountain day, vivid saturated natural colors",
        ],
        "stock_keywords": [
            "mountain", "alpine", "Dolomites", "Alps", "peaks", "landscape",
            "nature", "scenic", "snow", "rocky", "elevation", "majestic", "real"
        ],
    },
    "granite_peaks": {
        "locations": [
            "Patagonia Torres del Paine Chile, jagged granite spires dramatic sky",
            "Canadian Rockies Banff, dramatic rocky peaks above turquoise lake",
            "Mont Blanc French Alps, massive glacier and real snow peak",
            "Himalayas Nepal, massive real snow peaks above real clouds",
            "New Zealand Southern Alps, snow peaks above real green valleys",
            "Lofoten Norway, jagged real peaks rising dramatically from dark sea",
            "Alaska Denali wilderness, massive real granite peak above tundra",
            "Yosemite Valley California, massive granite walls and domes",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_MOUNTAIN,
        "seasons": [
            "peak summer, real green lower slopes, snow on high granite peaks",
            "deep winter, snow-covered, brilliant real white peaks crisp sky",
            "peak autumn, real golden valley, snow on high peaks",
            "spring, fresh real green emerging, snow still on real peaks",
        ],
        "foregrounds": [
            "close wildflower bloom on rocky alpine ground, vivid colors",
            "mountain gravel fragments, natural irregular disorder",
            "alpine rock surface, natural lichen and weathering detail",
            "natural snow field in foreground, real peaks beyond",
            "glacial moraine rocks, varied natural sizes and colors",
            "mountain stream rocks, clear cold water over stones",
        ],
        "moods": [
            "dramatic real power, raw geological force",
            "epic real remote wilderness, untouched by humans",
            "peaceful high real altitude, profound natural silence",
            "brilliant vivid real mountain day, maximum natural clarity",
        ],
        "stock_keywords": [
            "mountain", "granite", "peaks", "Patagonia", "Rockies", "landscape",
            "nature", "scenic", "snow", "dramatic", "wilderness", "epic", "real"
        ],
    },
}
