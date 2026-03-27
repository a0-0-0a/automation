COMPOSITIONS_GRASS = [
    "wide angle, grass foreground, horizon beyond",
    "low angle on grass, sky above, horizon middle",
    "looking across rolling hills of grass, layers receding",
    "grass close-up foreground, open plain beyond",
    "aerial view looking down at grass patterns from above",
    "grass and sky equal halves, perfect natural horizon",
    "rolling hills of grass, no single focal point, just landscape",
    "grass path or clearing between taller grass, open space beyond",
]

DAYTIME = [
    "bright clear midmorning, vivid grass colors, sharp crisp shadows",
    "brilliant sunny midday, intense light, vivid saturated colors",
    "perfect clear afternoon, warm sun, sharp long natural shadows",
    "warm clear morning, vivid green or golden grass, vivid light",
    "clear sunny late morning, rich warm natural grass tones",
]
GOLDEN = [
    "golden hour, warm light, grass glowing vivid amber gold",
    "sunrise, warm first light raking across natural grass surface",
    "late afternoon golden light, warm side illumination on grass",
]
ALL_TIMES = DAYTIME + GOLDEN

GROUPS = {
    "open_steppe": {
        "locations": [
            "endless rolling golden natural grassland",
            "flat endless natural grass stretching to horizon",
            "windswept golden natural grass plains",
            "high altitude natural grass plateau",
            "open golden natural grass plateau",
            "rolling natural sea of tall grass",
            "flat treeless natural grass plain",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_GRASS,
        "seasons": [
            "peak summer, tall golden dry natural grass, bright clear sky",
            "spring, fresh short vivid green natural grass",
            "autumn, tawny brown dried natural grass, clear cold light",
            "early summer, mixed green and gold grass, rich warm tones",
        ],
        "foregrounds": [
            "close natural grass stems of varied height in gentle wind",
            "dried grass seed heads close-up, fine natural detail",
            "windswept flattened natural grass showing wind direction",
            "tussock grass clumps, varied natural rounded organic shapes",
            "mixed grass species, varied heights and natural textures",
        ],
        "moods": [
            "vast open endless, sky and natural grass only",
            "golden warmth, peaceful natural open plain",
            "windswept natural solitude, constant grass movement",
            "elemental natural simplicity, pure horizontal golden space",
        ],
        "stock_keywords": [
            "grassland", "steppe", "prairie", "open", "landscape", "nature",
            "golden", "grass", "plains", "horizon", "scenic", "meadow", "field"
        ],
    },
    "wildflower_meadow": {
        "locations": [
            "natural wildflowers above the cloud layer",
            "vivid natural orange rolling hills",
            "golden natural tussock slopes",
            "natural wildflowers and peaks",
            "natural wildflowers and open sky",
            "natural wildflowers and distant peaks",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_GRASS,
        "seasons": [
            "peak wildflower season, maximum vivid natural color",
            "spring bloom, fresh vivid natural wildflowers everywhere",
            "summer, rich saturated natural grass and flower colors",
            "late spring, peak natural color and freshness",
        ],
        "foregrounds": [
            "mixed natural wildflowers of different heights and colors",
            "natural grass and small wildflowers, organic natural disorder",
            "natural grass close-up, warm backlit golden natural tones",
            "single wildflower bloom, soft natural blurred background",
        ],
        "moods": [
            "vibrant natural abundance, vivid saturated colors",
            "peaceful warm natural meadow, organic natural richness",
            "fresh alive wildflower season, pure natural joy",
            "golden warmth, natural wildflower and grass beauty",
        ],
        "stock_keywords": [
            "meadow", "wildflowers", "flowers", "field", "nature", "spring",
            "bloom", "colorful", "landscape", "scenic", "natural", "grass"
        ],
    },
}
