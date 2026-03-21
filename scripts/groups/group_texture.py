COMPOSITIONS_TEXTURE = [
    "texture fills entire frame, no horizon visible",
    "close macro view, texture as abstract natural composition",
    "slight diagonal angle, texture receding into distance",
    "flat top-down view, texture as natural pattern",
    "texture with natural shadow adding depth and dimension",
    "extreme close view, texture detail filling entire frame",
]

DAYTIME = [
    "bright clear natural light, maximum texture and detail visibility",
    "warm natural side light raking across surface revealing texture",
    "bright natural daylight, vivid natural color saturation",
    "soft diffused natural light, even natural texture rendering",
]
ALL_TIMES = DAYTIME

GROUPS = {
    "rock_stone_texture": {
        "locations": [
            "sandstone rock surface, layered warm natural color bands",
            "weathered granite surface, natural speckled mineral texture",
            "layered sedimentary rock face, varied natural color strata",
            "smooth canyon sandstone wall, warm natural color gradient",
            "lichen-covered rock surface, varied natural texture colors",
            "rough volcanic lava surface, dark natural textured pattern",
            "river-worn boulder surface, smooth natural stone texture",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_TEXTURE,
        "seasons": [
            "dry conditions, vivid natural rock colors, maximum clarity",
            "summer, vivid saturated natural rock colors",
            "warm dry season, maximum natural color and detail",
        ],
        "foregrounds": [
            "rock texture fills entire frame, extreme natural detail",
            "close view, natural rock surface patterns and minerals",
            "macro natural rock detail, mineral variations clearly visible",
            "layered rock close-up, natural geological history visible",
        ],
        "moods": [
            "ancient geological time, deep natural patterns",
            "warm rich tones, pure natural rock beauty",
            "abstract natural art, rock as design element",
            "timeless natural material, pure geological texture",
        ],
        "stock_keywords": [
            "texture", "rock", "stone", "background", "natural", "pattern",
            "surface", "geological", "abstract", "material", "design", "close-up"
        ],
    },
    "earth_sand_texture": {
        "locations": [
            "desert sand close-up, precise natural wind ripple patterns",
            "cracked dry earth, natural organic polygon crack patterns",
            "dried mud flat, natural organic cracked texture patterns",
            "white salt crystal formation, natural geometric patterns",
            "fine desert dust surface, natural color and grain texture",
            "desert pebble field, mixed natural stone colors and sizes",
        ],
        "times": ALL_TIMES,
        "compositions": COMPOSITIONS_TEXTURE,
        "seasons": [
            "dry season, vivid natural colors, maximum natural contrast",
            "after rain, dark wet natural surface, rich vivid colors",
            "summer, maximum natural color saturation, clear light",
        ],
        "foregrounds": [
            "natural texture fills entire frame, extreme close detail",
            "close view, natural organic surface patterns",
            "macro natural detail, tiny natural structures revealed",
            "intimate close view, natural texture as full composition",
        ],
        "moods": [
            "clean minimal, natural texture as pure design element",
            "rich natural detail, organic natural beauty",
            "warm earthy tones, pure natural material feel",
            "abstract natural pattern, design-ready background",
        ],
        "stock_keywords": [
            "texture", "sand", "earth", "background", "pattern", "natural",
            "surface", "abstract", "design", "organic", "cracked", "material"
        ],
    },
}
