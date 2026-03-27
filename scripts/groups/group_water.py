COMPOSITIONS_WATER = [
    "wide angle, water fills foreground, mountains or cliffs in background",
    "shoreline diagonal, water one side, land other side",
    "waterfall central, rock walls on both sides",
    "river winding through landscape, aerial view from above",
    "close view of water surface, natural reflection and ripples",
    "water and sky reflection, horizon in middle of frame",
    "cascading terraced pools, viewed from above and side",
    "lake edge, still water foreground, landscape beyond",
]

DAYTIME = [
    "bright clear midmorning, natural vivid water color, realistic crisp light",
    "perfect calm morning, mirror-still water, natural crystal clear reflection",
    "bright clear afternoon, natural realistic water color, not oversaturated",
    "clear sunny midday, natural vivid water color, calm still natural water",
]
GOLDEN = [
    "golden hour, natural warm realistic light on water, natural long reflections",
    "sunrise, natural soft pink sky reflected in still water, realistic tones",
    "late afternoon natural golden light on water, warm realistic tones",
]
ALL_TIMES = DAYTIME + GOLDEN

GROUPS = {
    "glacial_lakes": {
        "locations": [
            "vivid turquoise glacial lake mountains",
            "cascading vivid turquoise terraced pools",
            "milky vivid turquoise water mountains",
            "vivid turquoise water rocky valley peaks",
            "crystal clear deep vivid blue surface",
            "mirror-still dark fjord water cliffs",
            "deep mirror still water vertical cliffs",
            "clear turquoise water mountain backdrop",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_WATER,
        "seasons": [
            "summer, clear natural vivid water, maximum natural color",
            "autumn, natural golden reflections in perfectly still water",
            "spring, fresh natural clear light, clean high natural water",
            "winter clear day, thin natural ice forming at edges, crisp light",
        ],
        "foregrounds": [
            "smooth natural water-worn stones on shoreline, varied sizes",
            "clear natural shallow water over detailed rocky bottom",
            "natural pebbles at water edge, wet and dry contrast",
            "wet natural rocks at waterline, varied texture and color",
            "natural gravel bar, fine and coarse stones, clear water",
        ],
        "moods": [
            "perfectly still, natural glassy reflection, profound calm",
            "vivid natural turquoise color, rich clear natural water",
            "peaceful natural lakeside calm, clear natural reflections",
            "cool natural fresh water, clean perfect natural clarity",
        ],
        "stock_keywords": [
            "lake", "turquoise", "reflection", "mountain lake", "alpine",
            "water", "calm", "mirror", "nature", "scenic", "crystal", "serene"
        ],
    },
    "waterfalls_rivers": {
        "locations": [
            # ✅ removed Iceland glacial river from autumn golden season
            # Iceland has no golden autumn trees — replaced with better locations
            "dramatic cascading real waterfall cliffs",
            "vivid turquoise cascading water",
            "dramatic waterfall rocky cliff autumn",
            "cascading real waterfall dark cliff",
            "massive real waterfall open plain",
            "dramatic real waterfall deep canyon",
            "massive granite waterfall, forest below",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_WATER,
        "seasons": [
            "spring, high natural water, turbulent vivid natural flow",
            "summer, clear natural vivid water, rich natural color",
            # ✅ autumn only for locations that actually have autumn foliage
            "autumn, golden deciduous trees surrounding clear natural water",
            "winter, partially frozen waterfall, dramatic natural ice formations",
        ],
        "foregrounds": [
            "natural river gravel bar, fine to coarse naturally sorted stones",
            "smooth natural water-worn boulders, clear natural water rushing",
            "natural river pebbles close-up, varied natural colors shapes",
            "clear natural shallow river water, complex rocky bottom detail",
            "wet natural rocks beside river, varied texture and color",
        ],
        "moods": [
            "flowing constant natural movement, water in natural motion",
            "dramatic natural waterfall power, nature force",
            "cool natural fresh clarity, clean natural river atmosphere",
            "vivid natural water color, rich natural beauty",
        ],
        "stock_keywords": [
            "waterfall", "river", "water", "flowing", "cascade", "nature",
            "stream", "rapids", "scenic", "landscape", "fresh water", "vivid"
        ],
    },
}
