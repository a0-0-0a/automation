import random

SEO_DATA = {
    "golden_sky": {
        "title_patterns": [
            "{adj} Sky at {time}",
            "{adj} {time} Sky Over Open Horizon",
            "Warm {adj} Sky {time} Glow",
            "{adj} {time} Skyline Natural Colors",
            "Vivid {adj} Sky {descriptor}",
            "{adj} Horizon {time} Light",
            "Natural {adj} Sky {time} View",
            "{adj} Sunset Sky Wide Panorama",
        ],
        "adj":        ["Golden", "Blazing", "Fiery", "Radiant", "Amber", "Copper", "Rich", "Warm", "Glowing", "Deep"],
        "time":       ["Sunset", "Dusk", "Golden Hour", "Twilight", "Dawn", "Evening"],
        "descriptor": ["Natural Glow", "Warm Light", "Dramatic Colors", "Wide View", "Open Horizon"],
        "descriptions": [
            "A breathtaking golden sky fills the frame with rich warm tones of amber, orange, and deep gold at golden hour. Perfect for backgrounds, editorial, and commercial nature projects.",
            "Warm golden hour light transforms the sky into a dramatic canvas of rich natural colors. Ideal for travel editorial, digital backgrounds, and wallpapers.",
            "Vivid warm tones sweep across the open sky, creating a stunning natural display of color and atmosphere. Perfect for commercial and editorial use.",
            "Rich amber and golden tones dominate the sky at sunset, casting warm natural light across the open landscape. Ideal for premium wallpapers and nature collections.",
        ],
        "keywords_core": [
            "golden sky", "sunset", "golden hour", "warm light", "amber sky",
            "orange sky", "horizon", "dusk", "twilight", "natural light",
            "dramatic sky", "glowing sky", "fiery sunset", "evening sky",
            "warm tones", "sky photography", "atmospheric", "sky colors",
            "sky background", "sky wallpaper", "cinematic sky", "wide sky",
            "panoramic sky", "scenic sky", "colorful sky", "vivid sky",
            "open horizon", "natural glow", "radiant sky", "warm atmosphere",
        ],
        "category": "Nature",
    },

    "dramatic_clouds": {
        "title_patterns": [
            "{adj} {subject} Over {landscape}",
            "{adj} {subject} {descriptor}",
            "Massive {adj} {subject} Natural Drama",
            "{adj} {subject} Wide Open Sky",
            "Epic {subject} {descriptor}",
            "{adj} Cloudscape {descriptor}",
            "Sweeping {adj} {subject} Panorama",
            "Powerful {subject} {descriptor}",
        ],
        "adj":       ["Dramatic", "Massive", "Towering", "Epic", "Stormy", "Moody", "Billowing", "Sweeping", "Dark", "Wild"],
        "subject":   ["Clouds", "Cloudscape", "Storm Clouds", "Cloud Formation", "Cloud Cover"],
        "landscape": ["Open Plains", "Rolling Hills", "Open Terrain", "Wide Horizon", "Open Landscape"],
        "descriptor":["Dramatic Light", "Blue Sky", "Natural Drama", "Wide Horizon", "Open View"],
        "descriptions": [
            "Massive dramatic clouds tower over an open landscape, their forms sculpted by wind and light into breathtaking natural architecture. Perfect for editorial, commercial, and artistic projects.",
            "Sweeping cloud formations fill the frame with natural drama, creating an atmosphere of raw natural power. Perfect for backgrounds, wallpapers, and dramatic nature collections.",
            "Epic storm clouds gather over open terrain, their dark contrasts creating a powerful natural atmosphere. Ideal for dramatic backgrounds and editorial use.",
        ],
        "keywords_core": [
            "dramatic clouds", "storm clouds", "cloudscape", "dramatic sky",
            "moody sky", "cloud formation", "billowing clouds", "epic sky",
            "atmospheric", "cloud drama", "natural power", "open sky",
            "cloud photography", "dynamic clouds", "cloud layers",
            "sky mood", "powerful sky", "cinematic clouds", "wide sky",
            "cloud background", "sky wallpaper", "editorial clouds",
            "towering clouds", "sweeping clouds", "turbulent sky",
        ],
        "category": "Nature",
    },

    "glacial_lakes": {
        "title_patterns": [
            "{adj} Mountain Lake {descriptor}",
            "{adj} Lake {descriptor}",
            "Crystal {adj} Lake Reflection",
            "{adj} Still Water {descriptor}",
            "Mirror {adj} Lake Natural Beauty",
            "{adj} Alpine Lake {descriptor}",
            "Pristine {adj} Mountain Lake View",
            "{adj} Lake Waters {descriptor}",
        ],
        "adj":        ["Turquoise", "Crystal", "Vivid", "Pristine", "Still", "Deep", "Clear", "Serene", "Glassy", "Calm"],
        "descriptor": ["Perfect Reflection", "Rocky Shore", "Golden Light", "Morning Light", "Clear Sky", "Wide View", "Natural Colors", "Summer Light", "Autumn View"],
        "descriptions": [
            "A stunning glacial lake reflects surrounding peaks in perfectly still turquoise waters. Ideal for travel editorial, luxury backgrounds, and nature collections.",
            "Crystal clear mountain lake waters display vivid turquoise tones surrounded by dramatic rocky peaks. Perfect for editorial, travel advertising, and premium nature stock.",
            "Mirror-still alpine lake waters capture the surrounding landscape in perfect reflection. Ideal for luxury editorial, wallpapers, and premium nature collections.",
            "Deep turquoise glacial lake shimmers under natural light, its pristine clarity creating a stunning visual composition. Perfect for travel photography and premium backgrounds.",
        ],
        "keywords_core": [
            "glacial lake", "mountain lake", "turquoise water", "lake reflection",
            "still water", "mirror lake", "crystal clear water", "alpine lake",
            "pristine lake", "mountain reflection", "calm water", "serene lake",
            "lake photography", "blue water", "teal water", "glacial water",
            "lake landscape", "scenic lake", "tranquil water", "glassy surface",
            "natural lake", "wilderness lake", "lake wallpaper", "lake background",
        ],
        "category": "Landscapes",
    },

    "waterfalls_rivers": {
        "title_patterns": [
            "{adj} Waterfall Over {surface}",
            "{adj} Cascade {descriptor}",
            "Powerful {adj} Waterfall Natural Force",
            "{adj} River {descriptor}",
            "Rushing {adj} Water {descriptor}",
            "{adj} Waterfall {descriptor}",
            "Wild {adj} River Natural Flow",
            "{adj} Cascade Rocky {descriptor}",
        ],
        "adj":        ["Cascading", "Powerful", "Rushing", "Dramatic", "Wild", "Crystal", "Natural", "Dynamic", "Vivid", "Pristine"],
        "surface":    ["Rocky Cliffs", "Natural Stone", "Dark Rocks", "Ancient Rock", "Natural Cliff"],
        "descriptor": ["Natural Force", "Clear Water", "Mountain Setting", "Rocky Landscape", "Golden Light", "Summer Light", "Wide View", "Misty Gorge"],
        "descriptions": [
            "A dramatic waterfall cascades powerfully over rocky cliffs, its white rushing water contrasting beautifully against dark stone. Perfect for travel editorial and dramatic backgrounds.",
            "Clear mountain river water rushes over smooth natural rocks, creating dynamic patterns of white water. Ideal for adventure editorial, environmental projects, and nature stock.",
            "Powerful cascading water flows over natural rock formations, capturing the raw energy of wilderness. Perfect for backgrounds, wallpapers, and premium nature collections.",
        ],
        "keywords_core": [
            "waterfall", "cascade", "river", "rushing water", "flowing water",
            "white water", "rapids", "mountain river", "waterfall photography",
            "natural waterfall", "dramatic waterfall", "river flow",
            "rocky waterfall", "waterfall mist", "river landscape",
            "scenic waterfall", "waterfall background", "river background",
            "water wallpaper", "adventure photography", "water power",
            "flowing river", "clear water", "fresh water", "wild river",
        ],
        "category": "Nature",
    },

    "granite_peaks": {
        "title_patterns": [
            "{adj} Granite Peaks {descriptor}",
            "{adj} Mountain Peaks {descriptor}",
            "Towering {adj} Rocky Peaks {descriptor}",
            "{adj} Summit {descriptor}",
            "Epic {adj} Mountain Peaks View",
            "{adj} Rocky Mountain {descriptor}",
            "Dramatic {adj} Peaks {descriptor}",
            "Massive {adj} Granite Summit",
        ],
        "adj":        ["Dramatic", "Towering", "Rugged", "Epic", "Massive", "Jagged", "Bold", "Imposing", "Majestic", "Sharp"],
        "descriptor": ["Blue Sky", "Golden Light", "Snow Capped", "Clear Sky", "Wide View", "Panoramic View", "Summer Light", "Natural Beauty", "Dramatic Sky"],
        "descriptions": [
            "Towering granite peaks rise dramatically against a vivid sky, their rugged faces cutting an imposing silhouette across the horizon. Perfect for adventure editorial and dramatic backgrounds.",
            "Massive rocky mountain peaks dominate the landscape, capturing the raw beauty of high mountain wilderness. Ideal for outdoor brands, travel editorial, and premium nature stock.",
            "Epic granite peaks soar above the landscape, their sharp ridgelines and rocky faces creating a powerful natural spectacle. Perfect for wallpapers and commercial nature collections.",
        ],
        "keywords_core": [
            "granite peaks", "mountain peaks", "rocky peaks", "mountain summit",
            "dramatic mountains", "rugged mountains", "jagged peaks",
            "mountain landscape", "high peaks", "mountain photography",
            "rocky summit", "mountain scenery", "mountain background",
            "mountain wallpaper", "epic mountains", "majestic peaks",
            "towering mountains", "wilderness peaks", "remote mountains",
            "mountain vista", "mountain panorama", "mountain view",
        ],
        "category": "Landscapes",
    },

    "limestone_peaks": {
        "title_patterns": [
            "{adj} Limestone Peaks {descriptor}",
            "{adj} Rocky Cliffs {descriptor}",
            "Towering {adj} Limestone {descriptor}",
            "{adj} Karst Formation {descriptor}",
            "Dramatic {adj} Rock Peaks {descriptor}",
            "{adj} Mountain Cliffs {descriptor}",
            "Pale {adj} Rocky Peaks {descriptor}",
            "{adj} Limestone Summit View",
        ],
        "adj":        ["Dramatic", "Towering", "Sharp", "Jagged", "Epic", "Rugged", "Bold", "Imposing", "Ancient", "Pale"],
        "descriptor": ["Clear Sky", "Blue Sky", "Golden Light", "Wide View", "Panoramic", "Natural Beauty", "Warm Light", "Morning Light", "Dramatic Sky"],
        "descriptions": [
            "Dramatic limestone peaks rise sharply against a vivid blue sky, their pale rocky karst formations creating a breathtaking natural landscape. Perfect for travel editorial and nature collections.",
            "Towering limestone cliffs create a dramatic mountain landscape of extraordinary natural character. Ideal for editorial, travel photography, and commercial nature stock.",
            "Ancient karst formations rise dramatically above the landscape, their distinctive pale faces creating a stunning geological spectacle. Perfect for premium wallpapers and editorial use.",
        ],
        "keywords_core": [
            "limestone peaks", "karst peaks", "rocky peaks", "limestone cliffs",
            "karst formation", "limestone mountain", "rocky mountain",
            "jagged peaks", "dramatic peaks", "mountain landscape",
            "pale rock", "rock formation", "geological landscape",
            "mountain photography", "rocky landscape", "mountain scenery",
            "mountain vista", "scenic peaks", "mountain wallpaper",
            "stunning mountains", "beautiful peaks", "majestic peaks",
        ],
        "category": "Landscapes",
    },

    "saharan_dunes": {
        "title_patterns": [
            "{adj} Sand Dunes {descriptor}",
            "{adj} Desert Dunes {descriptor}",
            "Vast {adj} Dunes {descriptor}",
            "{adj} Dune Landscape {descriptor}",
            "Rolling {adj} Sand Dunes {descriptor}",
            "Endless {adj} Desert {descriptor}",
            "{adj} Sandy Desert {descriptor}",
            "Sweeping {adj} Dunes {descriptor}",
        ],
        "adj":        ["Golden", "Vast", "Rolling", "Warm", "Deep", "Sweeping", "Dramatic", "Pristine", "Smooth", "Rich"],
        "descriptor": ["Warm Light", "Golden Hour", "Sunset Glow", "Open Horizon", "Natural Curves", "Dramatic Shadows", "Clear Sky", "Wide Panorama", "Natural Colors"],
        "descriptions": [
            "Vast rolling sand dunes stretch to the horizon, their smooth surfaces catching warm golden light to create stunning patterns of light and shadow. Perfect for travel editorial and luxury advertising.",
            "Rich golden sand dunes create an endless sculptural landscape of natural curves, their warm sandy tones glowing in natural light. Ideal for commercial backgrounds and editorial collections.",
            "Sweeping desert dunes fill the frame with warm golden tones and dramatic natural shadows. Perfect for minimal art, wallpapers, and premium desert stock photography.",
        ],
        "keywords_core": [
            "sand dunes", "desert dunes", "golden dunes", "desert landscape",
            "sandy desert", "dune landscape", "rolling dunes", "vast dunes",
            "endless desert", "open desert", "desert scenery", "dune photography",
            "warm desert", "golden desert", "desert light", "dune shadows",
            "dune ridges", "dune curves", "smooth dunes", "natural dunes",
            "desert background", "dune wallpaper", "minimal landscape",
            "desert patterns", "sand patterns", "arid landscape",
        ],
        "category": "Nature",
    },

    "dramatic_sea_cliffs": {
        "title_patterns": [
            "{adj} Sea Cliffs {descriptor}",
            "{adj} Coastal Cliffs {descriptor}",
            "Towering {adj} Ocean Cliffs {descriptor}",
            "{adj} Rocky Cliffs {descriptor}",
            "Epic {adj} Sea Cliffs {descriptor}",
            "{adj} Cliff Face {descriptor}",
            "Wild {adj} Coastal Cliffs {descriptor}",
            "Dramatic {adj} Cliffs {descriptor}",
        ],
        "adj":        ["Dramatic", "Rugged", "Towering", "Epic", "Bold", "Imposing", "Wild", "Raw", "Massive", "Ancient"],
        "descriptor": ["Ocean View", "Blue Sea", "Rocky Shore", "Wide View", "Open Horizon", "Natural Power", "Clear Day", "Panoramic View", "Natural Beauty"],
        "descriptions": [
            "Dramatic sea cliffs rise powerfully from the ocean, their rugged rocky faces carved by natural erosion into breathtaking coastal formations. Perfect for travel editorial and dramatic backgrounds.",
            "Towering coastal cliffs command the ocean horizon with their imposing rocky presence. Ideal for outdoor editorial, travel photography, and commercial ocean stock.",
            "Epic sea cliffs rise above wild ocean waters, their sheer faces and dramatic scale creating a powerful natural spectacle. Perfect for dramatic wallpapers and premium coastal stock.",
        ],
        "keywords_core": [
            "sea cliffs", "coastal cliffs", "ocean cliffs", "dramatic cliffs",
            "rugged cliffs", "towering cliffs", "coastal scenery",
            "ocean scenery", "cliff landscape", "coastal landscape",
            "rocky coast", "ocean coast", "dramatic coast", "wild coast",
            "cliff edge", "coastal drama", "ocean power", "wave cliffs",
            "coastal erosion", "rocky shoreline", "coastal background",
            "ocean background", "cliff wallpaper", "ocean editorial",
            "stunning cliffs", "majestic cliffs", "imposing coast",
        ],
        "category": "Landscapes",
    },

    "beach_seascape": {
        "title_patterns": [
            "{adj} Ocean {descriptor}",
            "{adj} Coastal Scene {descriptor}",
            "Serene {adj} Seascape {descriptor}",
            "{adj} Sea View {descriptor}",
            "Pristine {adj} Ocean {descriptor}",
            "{adj} Coastal Waters {descriptor}",
            "Clear {adj} Sea {descriptor}",
            "{adj} Seascape Natural Beauty",
        ],
        "adj":        ["Peaceful", "Vivid", "Calm", "Crystal", "Serene", "Pristine", "Turquoise", "Clear", "Tranquil", "Natural"],
        "descriptor": ["Blue Horizon", "Rocky Shore", "Clear Sky", "Wide View", "Open Horizon", "Calm Waters", "Golden Light", "Summer Light", "Natural Colors", "Panoramic View"],
        "descriptions": [
            "A pristine coastal scene stretches across the frame with vivid blue-green ocean waters meeting natural shoreline in perfect clarity. Ideal for travel editorial and luxury backgrounds.",
            "Crystal clear ocean waters display vivid natural turquoise and deep blue tones along an unspoiled shoreline. Perfect for travel photography, relaxation themes, and commercial nature stock.",
            "Serene coastal waters stretch to the open horizon, their vivid natural tones creating a peaceful and beautiful seascape. Perfect for wallpapers, editorial, and premium coastal collections.",
        ],
        "keywords_core": [
            "seascape", "ocean", "beach", "coastal", "sea", "blue ocean",
            "turquoise sea", "clear water", "ocean view", "coastal view",
            "sea view", "peaceful ocean", "calm sea", "serene coast",
            "tranquil beach", "pristine coast", "vivid ocean",
            "ocean color", "coastal color", "ocean background",
            "beach background", "sea wallpaper", "coastal wallpaper",
            "travel photography", "coastal photography", "ocean landscape",
        ],
        "category": "Nature",
    },

    "temperate_forest": {
        "title_patterns": [
            "{adj} Forest {descriptor}",
            "{adj} Woodland {descriptor}",
            "Ancient {adj} Forest {descriptor}",
            "{adj} Tree Canopy {descriptor}",
            "Sunlit {adj} Forest {descriptor}",
            "{adj} Forest Interior {descriptor}",
            "Majestic {adj} Woodland {descriptor}",
            "{adj} Forest Light {descriptor}",
        ],
        "adj":        ["Ancient", "Sunlit", "Majestic", "Golden", "Deep", "Lush", "Dense", "Tall", "Atmospheric", "Serene"],
        "descriptor": ["Golden Light", "Light Shafts", "Dappled Light", "Morning Light", "Autumn Colors", "Green Canopy", "Natural Glow", "Wide View", "Natural Beauty", "Warm Light"],
        "descriptions": [
            "Ancient towering trees create a majestic forest where golden light filters through leaves to create stunning natural patterns. Perfect for nature editorial and premium forest stock.",
            "Dappled golden light filters through a dense forest canopy, illuminating the mossy floor and massive trunks. Ideal for wellness brands, wallpapers, and editorial collections.",
            "Shafts of warm natural light pierce through the forest canopy, creating an atmospheric and beautiful woodland scene. Perfect for commercial backgrounds and premium nature stock.",
        ],
        "keywords_core": [
            "forest", "woodland", "trees", "tree canopy", "forest light",
            "sunlit forest", "golden forest", "light beams", "light shafts",
            "dappled light", "forest floor", "mossy floor", "tree trunks",
            "ancient trees", "tall trees", "towering trees", "forest scenery",
            "forest background", "forest editorial", "forest photography",
            "green forest", "lush forest", "dense forest",
            "forest canopy", "canopy light", "old growth forest",
        ],
        "category": "Nature",
    },

    "wildflower_meadow": {
        "title_patterns": [
            "{adj} Wildflower Meadow {descriptor}",
            "{adj} Flower Field {descriptor}",
            "Blooming {adj} Meadow {descriptor}",
            "{adj} Wildflowers {descriptor}",
            "Colorful {adj} Meadow {descriptor}",
            "Lush {adj} Flower Field {descriptor}",
            "{adj} Blooming Meadow {descriptor}",
            "Vibrant {adj} Wildflowers {descriptor}",
        ],
        "adj":        ["Colorful", "Vivid", "Lush", "Golden", "Vibrant", "Natural", "Rich", "Wild", "Bright", "Fresh"],
        "descriptor": ["Spring Bloom", "Warm Light", "Blue Sky", "Open Landscape", "Natural Colors", "Wide View", "Golden Hour", "Summer Light", "Natural Beauty", "Open Field"],
        "descriptions": [
            "A vivid wildflower meadow bursts with natural color, hundreds of flowers creating a rich tapestry of tones. Perfect for spring editorial, nature collections, and lifestyle advertising.",
            "Natural wildflowers bloom across a sweeping meadow in a stunning display of natural color and abundance. Ideal for seasonal editorial, wellness brands, and commercial nature collections.",
            "Colorful wildflowers stretch across an open meadow under natural light, creating a vibrant and beautiful landscape. Perfect for wallpapers, backgrounds, and premium nature stock.",
        ],
        "keywords_core": [
            "wildflower meadow", "wildflowers", "flower meadow", "flower field",
            "blooming meadow", "spring meadow", "summer meadow",
            "colorful flowers", "vivid flowers", "natural flowers",
            "meadow landscape", "flower landscape", "open meadow",
            "rolling meadow", "meadow background", "flower background",
            "spring photography", "summer photography", "nature photography",
            "meadow photography", "bloom", "colorful meadow",
            "vibrant meadow", "lush meadow", "wildflower colors",
        ],
        "category": "Nature",
    },

    "tropical_forest": {
        "title_patterns": [
            "{adj} Rainforest {descriptor}",
            "{adj} Tropical Forest {descriptor}",
            "Dense {adj} Jungle {descriptor}",
            "{adj} Forest Canopy {descriptor}",
            "Lush {adj} Tropical {descriptor}",
            "{adj} Jungle Interior {descriptor}",
            "Ancient {adj} Rainforest {descriptor}",
            "Vivid {adj} Forest Canopy {descriptor}",
        ],
        "adj":        ["Lush", "Dense", "Vivid", "Deep", "Ancient", "Rich", "Wild", "Thick", "Verdant", "Vibrant"],
        "descriptor": ["Green Canopy", "Filtered Light", "Natural Beauty", "Wide View", "Vivid Colors", "Morning Light", "Natural Glow", "Deep Setting", "Atmospheric Light"],
        "descriptions": [
            "A dense tropical rainforest creates a vivid green world of layered vegetation, bathed in filtered green light. Perfect for tropical editorial, environmental projects, and premium stock.",
            "The tropical forest canopy forms an intricate ceiling of vivid green, with filtered light creating a magical atmosphere. Ideal for travel editorial and luxury backgrounds.",
            "Towering rainforest trees rise above dense tropical undergrowth, their canopy filtering natural light into beautiful patterns. Perfect for wallpapers and editorial nature collections.",
        ],
        "keywords_core": [
            "tropical forest", "rainforest", "jungle", "tropical canopy",
            "forest canopy", "green canopy", "lush vegetation", "dense forest",
            "tropical vegetation", "tropical light", "filtered light",
            "green light", "tropical scenery", "tropical landscape",
            "lush landscape", "tropical background", "rainforest background",
            "tropical photography", "jungle photography",
            "tropical green", "vivid green", "lush green", "dense green",
        ],
        "category": "Nature",
    },

    "rocky_desert": {
        "title_patterns": [
            "{adj} Desert {descriptor}",
            "{adj} Rock Formation {descriptor}",
            "Ancient {adj} Desert Rocks {descriptor}",
            "{adj} Rocky Desert {descriptor}",
            "Rugged {adj} Desert {descriptor}",
            "{adj} Desert Landscape {descriptor}",
            "Dramatic {adj} Rock Faces {descriptor}",
            "Vast {adj} Desert {descriptor}",
        ],
        "adj":        ["Rocky", "Rugged", "Dramatic", "Vast", "Ancient", "Bold", "Arid", "Raw", "Eroded", "Wild"],
        "descriptor": ["Warm Light", "Open Horizon", "Clear Sky", "Natural Colors", "Wide View", "Golden Light", "Dramatic Sky", "Natural Beauty", "Warm Atmosphere", "Panoramic View"],
        "descriptions": [
            "A dramatic rocky desert landscape stretches across the frame, ancient eroded formations rising under clear skies and intense natural light. Perfect for adventure editorial and dramatic backgrounds.",
            "Rugged desert rock formations create a powerful landscape of natural geological drama, their warm tones glowing in harsh natural light. Ideal for outdoor brands and dramatic wallpapers.",
            "Ancient desert rocks rise from the dry floor, their eroded forms and warm natural tones creating a timeless landscape. Perfect for commercial editorial and premium nature stock.",
        ],
        "keywords_core": [
            "rocky desert", "desert rocks", "rock formation", "desert landscape",
            "arid landscape", "desert scenery", "rocky landscape",
            "desert photography", "rock photography", "desert rock",
            "sandstone rock", "eroded rock", "desert formation",
            "geological formation", "natural formation", "desert background",
            "rock wallpaper", "desert editorial", "adventure photography",
            "dry landscape", "arid environment", "desert terrain",
            "warm rock", "golden rock", "red rock", "desert colors",
        ],
        "category": "Nature",
    },

    "open_steppe": {
        "title_patterns": [
            "{adj} Grassland {descriptor}",
            "{adj} Open Plains {descriptor}",
            "Endless {adj} Steppe {descriptor}",
            "{adj} Rolling Plains {descriptor}",
            "Wide {adj} Landscape {descriptor}",
            "{adj} Prairie {descriptor}",
            "Vast {adj} Open Terrain {descriptor}",
            "Sweeping {adj} Grassland {descriptor}",
        ],
        "adj":        ["Vast", "Wide", "Endless", "Golden", "Sweeping", "Open", "Rolling", "Dramatic", "Wild", "Expansive"],
        "descriptor": ["Golden Horizon", "Open Sky", "Dramatic Sky", "Wide View", "Natural Colors", "Clear Sky", "Warm Light", "Open Horizon", "Natural Beauty", "Panoramic View"],
        "descriptions": [
            "A vast open grassland stretches endlessly to the horizon under a sweeping sky, creating a powerful sense of natural openness. Perfect for minimal editorial and dramatic landscape collections.",
            "Endless rolling plains of natural grassland create a sweeping minimal landscape, the wide horizon conveying freedom and space. Ideal for advertising, dramatic backgrounds, and wallpapers.",
            "Open steppe landscape stretches to the wide horizon under dramatic skies, its rolling natural terrain creating a powerful sense of scale. Perfect for commercial and editorial nature stock.",
        ],
        "keywords_core": [
            "grassland", "steppe", "open plains", "open landscape",
            "prairie", "rolling hills", "wide landscape", "vast landscape",
            "endless plains", "open horizon", "wide horizon",
            "grassland photography", "steppe photography", "plains photography",
            "open scenery", "vast scenery", "minimal landscape",
            "open background", "grassland background", "steppe wallpaper",
            "nature editorial", "landscape photography", "outdoor photography",
            "golden grass", "dry grass", "green grass", "grass texture",
        ],
        "category": "Landscapes",
    },

    "rock_stone_texture": {
        "title_patterns": [
            "{adj} Rock Texture {descriptor}",
            "{adj} Stone Surface {descriptor}",
            "Natural {adj} Rock {descriptor}",
            "{adj} Stone Texture {descriptor}",
            "Ancient {adj} Rock Surface {descriptor}",
            "{adj} Geological Texture {descriptor}",
            "Organic {adj} Stone {descriptor}",
            "{adj} Rock Pattern {descriptor}",
        ],
        "adj":        ["Natural", "Ancient", "Rough", "Rugged", "Layered", "Organic", "Textured", "Raw", "Rich", "Detailed"],
        "descriptor": ["Natural Pattern", "Natural Detail", "Close View", "Natural Light", "Warm Tones", "Organic Patterns", "Wide Shot", "Natural Beauty", "Surface Detail"],
        "descriptions": [
            "Close natural rock surface reveals extraordinary detail in its texture and organic patterns, creating a compelling natural abstract composition. Perfect for texture backgrounds and design resources.",
            "Ancient stone surface captures the geological history of natural rock in extraordinary visual detail. Ideal for design backgrounds, texture libraries, and commercial texture stock.",
            "Natural rock face displays rich organic patterns and varied tones in striking visual detail. Perfect for texture backgrounds, architectural inspiration, and premium design resources.",
        ],
        "keywords_core": [
            "rock texture", "stone texture", "natural texture", "rock surface",
            "stone surface", "rock pattern", "stone pattern",
            "geological texture", "natural stone", "rock detail",
            "stone detail", "texture photography", "rock photography",
            "stone photography", "natural material", "organic texture",
            "surface texture", "rough texture", "rugged texture",
            "textured background", "stone background", "rock background",
            "texture wallpaper", "design texture", "abstract texture",
            "natural abstract", "layered rock", "layered stone",
        ],
        "category": "Backgrounds",
    },

    "earth_sand_texture": {
        "title_patterns": [
            "{adj} Sand Texture {descriptor}",
            "{adj} Earth Surface {descriptor}",
            "Natural {adj} Sand {descriptor}",
            "{adj} Desert Surface {descriptor}",
            "Fine {adj} Earth Texture {descriptor}",
            "{adj} Sand Pattern {descriptor}",
            "Minimal {adj} Earth {descriptor}",
            "{adj} Sandy Surface {descriptor}",
        ],
        "adj":        ["Natural", "Fine", "Smooth", "Organic", "Minimal", "Pure", "Sandy", "Warm", "Dry", "Rich"],
        "descriptor": ["Natural Pattern", "Natural Detail", "Close View", "Natural Light", "Warm Tones", "Earth Tones", "Organic Patterns", "Wide Shot", "Natural Colors", "Desert Setting"],
        "descriptions": [
            "Fine natural sand and earth surface reveals beautiful organic patterns in extraordinary visual detail, creating a compelling minimal natural composition. Perfect for texture backgrounds and design resources.",
            "Natural desert sand and earth surface captures organic patterns and textures in rich detail. Ideal for design backgrounds, minimal art, and commercial texture stock collections.",
            "Sandy earth surface displays intricate natural grain patterns and warm earth tones in beautiful visual detail. Perfect for texture libraries, minimal editorial, and premium design resources.",
        ],
        "keywords_core": [
            "sand texture", "earth texture", "natural texture", "sand surface",
            "earth surface", "sand pattern", "earth pattern", "desert texture",
            "desert sand", "fine sand", "sand grain", "earth grain",
            "texture photography", "sand photography", "earth photography",
            "natural material", "organic texture", "surface texture",
            "fine texture", "smooth texture", "minimal texture",
            "textured background", "sand background", "earth background",
            "texture wallpaper", "minimal wallpaper", "design texture",
            "natural abstract", "sand abstract", "earth tones",
        ],
        "category": "Backgrounds",
    },
}


def generate_seo_title(group_name):
    """يولّد عنوان SEO عشوائي فريد وطبيعي لكل group"""
    if group_name not in SEO_DATA:
        return f"Natural {group_name.replace('_', ' ').title()} Landscape"

    data    = SEO_DATA[group_name]
    pattern = random.choice(data["title_patterns"])

    # نملأ الـ pattern بكلمات عشوائية
    title = pattern
    if "{adj}" in title:
        title = title.replace("{adj}", random.choice(data["adj"]))
    if "{time}" in title:
        title = title.replace("{time}", random.choice(data.get("time", ["Sunrise", "Sunset", "Golden Hour"])))
    if "{descriptor}" in title:
        title = title.replace("{descriptor}", random.choice(data["descriptor"]))
    if "{subject}" in title:
        title = title.replace("{subject}", random.choice(data.get("subject", ["Landscape"])))
    if "{landscape}" in title:
        title = title.replace("{landscape}", random.choice(data.get("landscape", ["Open Terrain"])))
    if "{surface}" in title:
        title = title.replace("{surface}", random.choice(data.get("surface", ["Rocky Surface"])))

    return title.strip()


def get_seo_data(group_name):
    """يرجع الـ SEO data الكاملة لكل group"""
    return SEO_DATA.get(group_name, None)
