# List of valid topics and canonicalization & generalization mappings
# for topics
#
# Copyright (c) 2020-2021 Tatu Ylonen.  See file LICENSE and https://ylonen.org

# Set of valid topic tags.  (Other tags may be canonicalized to these)
valid_topics = set([
    "Catholicism",
    "Christianity",
    "Internet",
    "aeronautics",
    "aerospace",
    "agriculture",
    "anatomy",
    "animal",
    "anthropology",
    "arachnology",
    "archeology",
    "architecture",
    "arithmetic",
    "arts",
    "astrology",
    "astronomy",
    "astrophysics",
    "ball-games",
    "biochemistry",
    "biology",
    "board-games",
    "botany",
    "broadcasting",
    "business",
    "card-games",
    "carpentry",
    "cartography",
    "cause",
    "chemistry",
    "cities",
    "color",
    "combinatorics",
    "commerce",
    "communications",
    "computing",
    "construction",
    "cooking",
    "copyright",
    "cosmology",
    "countries",
    "court",
    "crafts",
    "criminology",
    "cryptocurrency",
    "cryptography",
    "cuisine",
    "demography",
    "dancing",
    "dentistry",
    "diving",
    "dogs",
    "drama",
    "drugs",
    "ecology",
    "economics",
    "education",
    "electrical-engineering",
    "electricity",
    "electromagnetism",
    "energy",
    "engineering",
    "entomology",
    "epistemology",
    "error",
    "ethnography",
    "falconry",
    "fantasy",
    "fashion",
    "film",
    "finance",
    "food",
    "football",
    "fortifications",
    "games",
    "gemology",
    "geography",
    "geology",
    "geometry",
    "government",
    "hairdressing",
    "heading",
    "healthcare",
    "histology",
    "history",
    "hobbies",
    "horology",
    "horses",
    "human-sciences",
    "hunting",
    "hydrology",
    "ichthyology",
    "ideology",
    "information",
    "jewelry",
    "journalism",
    "law",
    "lifestyle",
    "linguistics",
    "literature",
    "location",
    "mammals",
    "management",
    "manner",
    "manufacturing",
    "marketing",
    "martial-arts",
    "masonry",
    "mathematics",
    "meats",
    "mechanical-engineering",
    "media",
    "medicine",
    "metallurgy",
    "meteorology",
    "metrology",
    "microbiology",
    "military",
    "mineralogy",
    "mining",
    "monarchy",
    "morphology",
    "music",
    "mysticism",
    "mythology",
    "natural-sciences",
    "naturism",
    "nautical",
    "navy",
    "neurology",
    "neuroscience",
    "nobility",
    "oceanography",
    "oenology",
    "organization",
    "origin",
    "ornithology",
    "paleontology",
    "pathology",
    "performing-arts",
    "petrology",
    "pharmacology",
    "philosophy",
    "phonology",
    "photography",
    "physical-sciences",
    "physics",
    "physiology",
    "planets",
    "political-science",
    "politics",
    "programming",
    "position",
    "publishing",
    "pulmonology",
    "prefectures",
    "printing",
    "property",
    "pseudoscience",
    "psychiatry",
    "psychology",
    "radio",
    "radiology",
    "railways",
    "region",
    "religion",
    "science-fiction",
    "sciences",
    "sexuality",
    "skating",
    "skiing",
    "social-science",
    "socialism",
    "sociology",
    "software",
    "source",
    "sports",
    "state",
    "states",
    "statistics",
    "taxonomy",
    "telecommunications",
    "telegraphy",
    "telephony",
    "television",
    "temperature",
    "textiles",
    "theater",
    "theology",
    "time",
    "tools",
    "topology",
    "tourism",
    "toxicology",
    "transport",
    "typography",
    "units-of-measure",
    "vehicles",
    "video-games",
    "visual-arts",
    "weaponry",
    "weather",
    "weekdays",
    "wrestling",
    "writing",
    "zoology",
])

# Translation map for topics.
# XXX revisit this mapping.  Create more fine-tuned hierarchy
# XXX or should probably not try to generalize here
topic_generalize_map = {
    "(sport)": "sports",
    "card games": "games",
    "cards": "card-games",
    "board-games": "games",
    "game of Go": "board-games",
    "Scrabble": "board-games",
    "ball games": "ball-games",
    "ball-games": "games",
    "dice": "games",
    "rock paper scissors": "games",
    '"manner of action"': "manner",
    "manner of action": "manner",
    "planets of the Solar system": "planets",
    "planets": "astronomy region",
    "continents": "geography region",
    "countries of Africa": "countries",
    "countries of Europe": "countries",
    "countries of Asia": "countries",
    "countries of South America": "countries",
    "countries of North America": "countries",
    "countries of Central America": "countries",
    "countries of Oceania": "countries",
    "countries": "region",
    "country": "countries",
    "the country": "countries",
    "regions of Armenia": "region",
    "region around the Ruppel river": "region",
    "geographical region": "region",
    "winegrowing region": "region",
    "the historical region": "region",
    "region": "geography location",
    "geography": "sciences",
    "natural-sciences": "sciences",
    "states of India": "states",
    "states of Australia": "states",
    "states": "region",
    "city": "cities",
    "cities": "region",
    "prefectures of Japan": "prefectures",
    "prefecture": "region",
    "software": "computing",
    "Windows": "software",
    "Linux": "software",
    "text messaging": "communications telephony",
    "secret": "information",
    "mail": "information",
    "information": "communications",
    "billiards": "games",
    "blackjack": "games",
    "backgammon": "games",
    "bridge": "games",
    "darts": "games",
    "human-sciences": "sciences",
    "anthropology": "human-sciences",
    "anthropodology": "anthropology",
    "ornithology": "biology",
    "ornitology": "ornithology",
    "birdwatching": "ornithology",
    "entomology": "biology",
    "insects": "entomology",
    "medicine": "sciences",
    "anatomy": "medicine",
    "Anatomy": "anatomy",
    "health": "medicine",
    "emergency medicine": "medicine",
    "bone": "anatomy",
    "body": "anatomy",
    "scientific": "sciences",
    "scholarly": "sciences",
    "neuroanatomy": "anatomy neurology",
    "neurotoxicology": "neurology toxicology",
    "neurobiology": "neurology",
    "neurophysiology": "physiology neurology",
    "nephrology": "medicine",
    "hepatology": "medicine",
    "endocrinology": "medicine",
    "gynaecology": "medicine",
    "mammology": "medicine",
    "urology": "medicine",
    "neurology": "medicine neuroscience",
    "neuroscience": "human-sciences",
    "gerontology": "medicine",
    "andrology": "medicine",
    "phycology": "botany",
    "planktology": "botany",
    "oncology": "medicine",
    "hematology": "medicine",
    "physiology": "medicine",
    "gastroenterology": "medicine",
    "surgery": "medicine",
    "opthalmology": "medicine",
    "pharmacology": "medicine",
    "drugs": "pharmacology",
    "cytology": "biology medicine",
    "healthcare": "government",
    "cardiology": "medicine",
    "dentistry": "medicine",
    "odontology": "dentistry",
    "pathology": "medicine",
    "toxicology": "medicine",
    "dermatology": "medicine",
    "epidemiology": "medicine",
    "psychiatry": "medicine psychology",
    "psychoanalysis": "medicine psychology",
    "phrenology": "medicine psychology",
    "psychology": "medicine human-sciences",
    "sociology": "social-science",
    "social science": "social-science",
    "social sciences": "social-science",
    "in transactional analysis": "social-science",
    "social-science": "human-sciences",
    "hydraulics": "engineering",
    "demographics": "demography",
    "immunology": "medicine",
    "immunologic sense": "medicine",
    "anesthesiology": "medicine",
    "xenobiology": "biology",
    "sinology": "geography",
    "psychopathology": "psychiatry",
    "histopathology": "pathology histology",
    "histology": "biology",
    "patology": "pathology",
    "virology": "medicine",
    "bacteriology": "medicine",
    "parapsychology": "psychology pseudoscience",
    "psyschology": "psychology error",
    "printing technology": "printing",
    "litography": "printing",
    "iconography": "history",
    "geomorphology": "geology",
    "phytopathology": "botany pathology",
    "bryology": "botany",
    "opthalmology": "medicine",
    "embryology": "medicine",
    "illness": "medicine",
    "parasitology": "medicine",
    "teratology": "medicine",
    "speech therapy": "medicine",
    "speech pathology": "medicine",
    "radiology": "medicine",
    "radiography": "radiology",
    "vaccinology": "medicine",
    "traumatology": "medicine",
    "microbiology": "biology medicine",
    "pulmonology": "medicine",
    "obstetrics": "medicine",
    "pneumology": "pulmonology",
    "biology": "natural-sciences",
    "strong topology": "topology",
    "sociobiology": "social-science biology",
    "radio technology": "electrical-engineering radio",
    "authorship": "copyright",
    "volcanology": "geology",
    "gemmology": "gemology",
    "gem-cutting": "jewelry",
    "gemology": "geology jewelry",
    "jewelry": "lifestyle",
    "conchology": "zoology",
    "comics": "literature",
    "codicology": "history",
    "zoology": "biology",
    "zootomy": "zoology",
    "botany": "biology",
    "malacology": "biology",
    "taxonomy": "biology",
    "biological category": "taxonomy",
    "geology": "geography",
    "mineralogy": "geology chemistry",
    "mineralology": "mineralogy",
    "biochemistry": "microbiology chemistry",
    "immunochemistry": "biochemistry",
    "petrochemistry": "chemistry",
    "language": "linguistics",
    "grammar": "linguistics",
    "syntax": "linguistics",
    "semantics": "linguistics",
    "epistemology": "philosophy",
    "ontology": "epistemology",
    "etymology": "linguistics",
    "ethnology": "anthropology",
    "ethnography": "anthropology",
    "historical ethnography": "ethnography history",
    "entertainment industry": "economics",
    "electrochemistry": "chemistry",
    "classical studies": "history",
    "textual criticism": "linguistics",
    "nanotechnology": "engineering",
    "electromagnetism": "physics",
    "biotechnology": "engineering medicine",
    "systems theory": "mathematics",
    "computer games": "games",
    "graphic design": "arts",
    "criminology": "law human-sciences",
    "penology": "criminology",
    "pragmatics": "linguistics",
    "morphology": "linguistics",
    "phonology": "linguistics",
    "phonetics": "phonology",
    "prosody": "phonology",
    "lexicography": "linguistics",
    "lexicology": "linguistics",
    "narratology": "linguistics",
    "linguistic": "linguistics",
    "translation studies": "linguistics",
    "semiotics": "linguistics",
    "dialectology": "linguistics",
    "ortography": "linguistics",
    "typography": "publishing",
    "letterpress typography": "typography",
    "psycholinguistics": "linguistics psychology",
    "sociolinguistics": "linguistics sociology",
    "beekeeping": "agriculture",
    "officialese": "government",
    "hairdressing": "crafts",
    "wagonmaking": "crafts",
    "smithwork": "crafts",
    "papermaking": "crafts",
    "hairstyle": "hairdressing",
    "textiles": "manufacturing",
    "weaving": "textiles",
    "quilting": "textiles",
    "knitting": "textiles",
    "sewing": "textiles",
    "cutting": "textiles",
    "furniture": "manufacturing lifestyle",
    "freemasonry": "lifestyle",
    "caving": "sports",
    "country dancing": "dancing",
    "dance": "dancing",
    "dancing": "sports",
    "hip-hop": "dancing",
    "cheerleading": "sports",
    "bowling": "sports",
    "athletics": "sports",
    "performing-arts": "arts sports",
    "acrobatics": "performing-arts",
    "circus": "performing-arts",
    "juggling": "performing-arts",
    "martial arts": "martial-arts",
    "martial-arts": "sports",
    "judo": "martial-arts",
    "skydiving": "sports",
    "meterology": "meteorology",
    "meteorology": "geography",
    "weather": "meteorology",
    "climate": "meteorology",
    "cryptozoology": "zoology",
    "lepidopterology": "zoology",
    "nematology": "zoology",
    "campanology": "history",
    "vexillology": "history",
    "phenomenology": "philosophy",
    "seismology": "geology",
    "cosmology": "astronomy",
    "astrogeology": "astronomy geology",
    "areology": "astrology geology",
    "stratigraphy": "geology",
    "orography": "geology",
    "stenography": "writing",
    "graphonomics": "writing",
    "scriptwriting": "writing",
    "orthography": "writing",
    "palynology": "chemistry microbiology",
    "lichenology": "botany",
    "seasons": "weather",
    "information technology": "computing",
    "algebra": "mathematics",
    "calculus": "mathematics",
    "arithmetics": "mathematics",
    "statistics": "mathematics",
    "geometry": "mathematics",
    "logic": "mathematics philosophy",
    "trigonometry": "mathematics",
    "mathematical analysis": "mathematics",
    "ethics": "philosophy",
    "existentialism": "philosophy",
    "religion": "philosophy lifestyle",
    "philosophy": "human-sciences",
    "transport": "economics",
    "shipping": "economics",
    "railways": "vehicles",
    "trains": "railways",
    "automotive": "vehicles",
    "automobile": "vehicles",
    "vehicles": "transport",
    "tourism": "economics",
    "travel": "tourism lifestyle",
    "travel industry": "tourism",
    "parliamentary procedure": "government",
    "espionage": "government",
    "food": "lifestyle",
    "cuisine": "food",
    "Indian Chinese cuisine": "cuisine",
    "seafood": "cuisine",
    "vegetable": "food",
    "beer": "food",
    "brewing": "food manufacturing",
    "sewage treatment": "engineering",
    "cooking": "food",
    "baking": "cooking",
    "Indian cookery": "cooking",
    "sexuality": "lifestyle",
    "seduction community": "sexuality",
    "BDSM": "sexuality",
    "LGBT": "sexuality",
    "sexual orientations": "sexuality",
    "romantic orientations": "sexuality",
    "prostitution": "sexuality",
    "sexology": "sexuality",
    "biblical": "religion",
    "ecclesiastical": "religion",
    "genetics": "biology medicine",
    "medical terminology": "medicine",
    "opthalmology": "medicine",
    "homeopathy": "medicine",
    "mycology": "biology",
    "paganism": "religion",
    "Scientology": "religion",
    "mechanical-engineering": "engineering",
    "mechanics": "mechanical-engineering",
    "mechanical": "mechanical-engineering",
    "machining": "mechanical-engineering",
    "lubricants": "mechanical-engineering",
    "fasteners": "mechanical-engineering",
    "measurement": "property",
    "thermodynamics": "physics",
    "fluid dynamics": "physics",
    "signal processing": "computing mathematics",
    "topology": "mathematics",
    "algebraic topology": "topology",
    "algebraic geometry": "geometry",
    "norm topology": "topology",
    "linear algebra": "mathematics",
    "number theory": "mathematics",
    "insurance": "economics",
    "taxation": "economics government",
    "sugar-making": "manufacturing",
    "glassmaking": "manufacturing",
    "food manufacture": "manufacturing",
    "manufacturing": "economics",
    "optics": "physics engineering",
    "physical-sciences": "sciences",
    "chemistry": "physical-sciences",
    "ceramics": "chemistry engineering",
    "chess": "games",
    "checkers": "games",
    "mahjong": "games",
    "Rubik's Cube": "games",
    "crystallography": "chemistry",
    "fluids": "chemistry physics engineering",
    "science": "sciences",
    "physics": "physical-sciences",
    "electrical-engineering": "engineering",
    "electricity": "electrical-engineering physics",
    "electronics": "electrical-engineering",
    "programming": "computing",
    "Lisp": "programming",
    "databases": "computing",
    "visual art": "visual-arts",
    "visual arts": "visual-arts",
    "visual-arts": "arts",
    "graffiti": "visual-arts",
    "crafts": "arts hobbies",
    "papercraft": "crafts",
    "bowmaking": "crafts",
    "lutherie": "crafts",
    "ironworking": "crafts",
    "glassblowing": "crafts",
    "history": "human-sciences",
    "Egyptology": "history",
    "heraldry": "hobbies nobility",
    "philately": "hobbies",
    "hobbies": "lifestyle",
    "numismatics": "hobbies",
    "chronology": "horology",
    "horology": "hobbies",
    "cryptography": "computing",
    "encryption": "cryptography",
    "finance": "economics",
    "finances": "finance",
    "financial": "finance",
    "accounting": "finance",
    "microeconomics": "economics",
    "business": "economics",
    "politics": "government",
    "geopolitics": "politics",
    "communism": "ideology",
    "socialism": "ideology",
    "capitalism": "ideology",
    "feudalism": "politics",
    "fascism": "ideology",
    "white supremacist ideology": "ideology",
    "manosphere": "ideology",
    "pedology": "geography",
    "biogeography": "geography biology",
    "cryptocurrency": "finance",
    "nobility": "monarchy",
    "monarchy": "politics",
    "demography": "social-science statistics government",
    "historical demography": "demography",
    "chromatography": "chemistry",
    "anarchism": "politics",
    "diplomacy": "politics",
    "regionalism": "politics",
    "economic liberalism": "politics",
    "agri.": "agriculture",
    "agriculture": "lifestyle",
    "horticulture": "agriculture",
    "fashion": "lifestyle textiles",
    "cosmetics": "lifestyle",
    "design": "arts lifestyle",
    "money": "finance",
    "oceanography": "geography",
    "geological oceanography": "geology oceanography",
    "angelology": "theology",
    "woodworking": "carpentry",
    "art": "arts",
    "television": "broadcasting",
    "broadcasting": "media",
    "radio": "broadcasting",
    "radio communications": "radio",
    "radio technics": "radio",
    "journalism": "media",
    "writing": "journalism literature",
    "editing": "writing",
    "poetry": "writing",
    "film": "television",
    "cinematography": "film",
    "drama": "film theater",
    "printing": "publishing",
    "publishing": "media",
    "science fiction": "literature",
    "space science": "aerospace",
    "astronautics": "aerospace",
    "aerodynamics": "aerospace",
    "NASA": "aerospace",
    "fiction": "literature",
    "pornography": "media sexuality",
    "DVD": "media",
    "sex": "sexuality",
    "information science": "human-sciences",
    "naturism": "lifestyle",
    "veganism": "lifestyle",
    "urbanism": "lifestyle",
    "Kantianism": "philosophy",
    "newspapers": "journalism",
    "telegraphy": "telecommunications",
    "wireless telegraphy": "telegraphy",
    "telegram": "telegraphy",
    "audio": "radio television electrical-engineering",
    "literature": "publishing",
    "folklore": "arts history",
    "MMORPG": "Internet video-games",
    "ACG": "video-games",
    "Magic: The Gathering": "games",
    "IRC": "Internet",
    "CSS": "Internet",
    "blogging": "Internet",
    "music": "publishing arts",
    "baile funk": "music",
    "musical note": "music",
    "guitar": "music",
    "handbells": "music",
    "handball": "ball-games",
    "musicology": "music human-sciences",
    "MIDI": "music",
    "talking": "communications",
    "militaryu": "military",
    "army": "military",
    "navy": "military",
    "naval": "navy",
    "weaponry": "military tools",
    "weapon": "weaponry",
    "firearms": "weaponry",
    "artillery": "weaponry",
    "ballistics": "weaponry",
    "fortifications": "military",
    "fortification": "fortifications",
    "law enforcement": "government",
    "firefighting": "government",
    "archaeology": "history",
    "epigraphy": "history",
    "paleontology": "history natural-sciences",
    "palæontology": "paleontology",
    "paleobiology": "paleontology biology",
    "paleoanthropology": "paleontology anthropology",
    "paleogeography": "paleontology geography",
    "palentology": "paleontology error",
    "papyrology": "history",
    "hagiography": "history religion",
    "palaeography": "history",
    "historical geography": "geography history",
    "historiography": "history",
    "calligraphy": "arts",
    "crocheting": "crafts",
    "ichthyology": "zoology",
    "fish": "ichthyology",
    "herpetology": "zoology",
    "glaciology": "geography",
    "arachnology": "zoology",
    "mammals": "zoology",
    "rodents": "mammals",
    "snakes": "zoology",
    "veterinary pathology": "zoology pathology",
    "veterinary": "zoology pathology",
    "conservation": "biology history",
    "patology": "pathology",
    "acarology": "arachnology",
    "mythology": "human-sciences",
    "ufology": "mythology",
    "fundamental interactions": "physics",
    "quantum field theory": "physics",
    "colorimetry": "physics",
    "extragalactic medium": "cosmology",
    "extra-cluster medium": "cosmology",
    "uranography": "cartography astronomy",
    "astrocartography": "cartography astronomy",
    "mining": "manufacturing",
    "quarrying": "mining",
    "forestry": "manufacturing",
    "metalworking": "metallurgy crafts",
    "tin-plate mnufacture": "metallurgy",
    "metallurgy": "engineering",
    "brick-making": "engineering",
    "communication": "communications",
    "telecommunications": "electrical-engineering communications",
    "telephony": "telecommunications communications",
    "mobile telephony": "telephony",
    "telephone": "telephony",
    "bookbinding": "crafts publishing",
    "engraving": "crafts",
    "petrology": "geology",
    "petroleum": "petrology energy",
    "petrography": "petrology",
    "energy": "engineering physics",
    "shipbuilding": "manufacturing",
    "plumbing": "construction",
    "roofing": "construction",
    "carpentry": "construction",
    "construction": "manufacturing",
    "piledriving": "construction",
    "masonry": "construction",
    "stone": "masonry",
    "tools": "engineering",
    "cranes": "tools",
    "colleges": "education",
    "higher education": "education",
    "clothing": "textiles fashion",
    "dyeing": "textiles",
    "fabrics": "textiles",
    "alchemy": "pseudoscience",
    "photography": "hobbies arts",
    "videography": "photography film",
    "horses": "sports lifestyle",
    "equestrianism": "horses",
    "equestrian": "horses",
    "horseracing": "horses",
    "dressage": "horses",
    "dogs": "lifestyle",
    "sheepdog trials": "dogs",
    "demoscene": "computing",
    "golf": "sports lifestyle",
    "tennis": "sports",
    "hunting": "lifestyle agriculture",
    "fishing": "lifestyle agriculture",
    "birdwashing": "hobbies",
    "fisheries": "ecology",
    "climatology": "geography ecology",
    "limnology": "ecology",
    "informatics": "computing",
    "marketing": "business",
    "advertising": "marketing",
    "electrotechnology": "electrical-engineering",
    "electromagnetic radiation": "electromagnetism",
    "electronics manufacturing": "manufacturing electrical-engineering",
    "electric power": "energy electrical-engineering",
    "electronic communication": "telecommunications",
    "electrical device": "electrical-engineering",
    "enology": "oenology",
    "oenology": "food",
    "wine": "oenology lifestyle",
    "cigars": "lifestyle",
    "smoking": "lifestyle",
    "flowery": "lifestyle botany",
    "gambling": "games",
    "exercise": "sports",
    "football": "ball-games",
    "netball": "ball-games",
    "softball": "ball-games",
    "American football": "football",
    "acting": "drama",
    "theater": "arts",
    "comedy": "theater film",
    "dominoes": "games",
    "pocket billiards": "games",
    "pool": "games",
    "graphical user interface": "computing",
    "mysticism": "philosophy",
    "philology": "philosophy",
    "enthnology": "human-sciences",
    "feminism": "ideology",
    "creationism": "religion",
    "shamanism": "religion",
    "ideology": "politics philosophy",
    "politology": "political-science",
    "political-science": "human-sciences",
    "political science": "political-science",
    "cartomancy": "mysticism",
    "tarot": "mysticism",
    "tasseography": "mysticism",
    "occult": "mysticism",
    "theology": "religion",
    "religionists": "religion",
    "spiritualism": "religion",
    "demonology": "religion",
    "horse racing": "horses",
    "horse-racing": "horses",
    "equitation": "horses",
    "farriery": "horses",
    "motor racing": "sports",
    "racing": "sports",
    "spinning": "sports",
    "gymnastics": "sports",
    "cricket": "sports",
    "volleyball": "ball-games",
    "lacrosse": "ball-games",
    "rugby": "ball-games",
    "bodybuilding": "sports",
    "falconry": "hunting",
    "hawking": "falconry",
    "parachuting": "sports",
    "squash": "sports",
    "curling": "sports",
    "motorcycling": "sports",
    "swimming": "sports",
    "diving": "sports",
    "underwater diving": "diving",
    "basketball": "ball-games",
    "baseball": "ball-games",
    "pesäpallo": "ball-games",
    "soccer": "ball-games",
    "snooker": "sports",
    "snowboarding": "sports",
    "skateboarding": "sports",
    "weightlifting": "sports",
    "skiing": "sports",
    "alpine skiing": "skiing",
    "aerial freestyle": "skiing",
    "mountaineering": "sports",
    "skating": "sports",
    "ice hockey": "skating",
    "cycling": "sports",
    "rowing": "sports",
    "boxing": "martial-arts",
    "Scouting": "lifestyle",
    "bullfighting": "sports",
    "archery": "martial-arts",
    "fencing": "martial-arts",
    "climbing": "sports",
    "surfing": "sports",
    "ballooning": "sports",
    "sailmaking": "manufacturing nautical",
    "sailing": "nautical",
    "maritime": "nautical",
    "ropemaking": "manufacturing nautical",
    "retail": "commerce",
    "commercial": "commerce",
    "retailing": "commerce",
    "electrical": "electricity",
    "category theory": "mathematics computing",
    "in technical contexts": "engineering physics chemistry",
    "technology": "engineering",
    "technical": "engineering",
    "stock exchange": "finance",
    "stock market": "finance",
    "trading": "finance",
    "surveying": "geography",
    "networking": "computing",
    "computer sciences": "computing",
    "computer software": "computing",
    "software compilation": "computing",
    "computer languages": "computing",
    "computer hardware": "computing",
    "computer graphics": "computing",
    "meats": "food",
    "meat": "meats",
    "web design": "computing",
    "aviation": "aeronautics",
    "aerospace": "aeronautics",
    "rocketry": "aerospace",
    "investment": "finance",
    "computing theory": "computing mathematics",
    "information theory": "mathematics computing",
    "probability": "mathematics",
    "probability theory": "mathematics",
    "set theory": "mathematics",
    "sets": "mathematics",
    "order theory": "mathematics",
    "graph theory": "mathematics",
    "group theory": "mathematics",
    "complex analysis": "mathematics",
    "measure theory": "mathematics",
    "mathematical analysis": "mathematics",
    "combinatorics": "mathematics",
    "cellular automata": "computing mathematics",
    "game theory": "mathematics computing",
    "computational": "computing",
    "computer": "computing",
    "behavioral sciences": "psychology",
    "behavior": "psychology",
    "clinical psychology": "psychology",
    "psycology": "psychology",
    "space sciences": "astronomy",
    "applied sciences": "sciences engineering",
    "civil engineering": "engineering",
    "(sport)": "sports",
    "stock ticker symbol": "finance",
    "banking": "economics",
    "commerce": "economics",
    "cryptocurrency": "finance",
    "cryptocurrencies": "cryptocurrency",
    "cartography": "geography",
    "ecology": "biology",
    "hydrology": "geography",
    "hydrography": "hydrology oceanography",
    "hydrodynamics": "hydrology",
    "topography": "geography",
    "bibliography": "history literature",
    "polygraphy": "law",
    "planetology": "astronomy",
    "astrology": "mysticism",
    "astrology signs": "astrology",
    "linguistic morphology": "morphology",
    "science": "sciences",
    "console": "video-games",
    "video games": "video-games",
    "role-playing games": "games",
    "poker": "card-games",
    "waterpolo": "games",
    "wrestling": "martial-arts",
    "professional wrestling": "wrestling",
    "sumo": "wrestling",
    "legal": "law",
    "copyright": "law",
    "intellectual property": "law",
    "court": "law government",
    "rail transport": "railways",
    "traffic": "transport",
    "incoterm": "transport",
    "road": "transport",
    "colour": "color",
    "color": "property",
    "time": "property",
    "days of the week": "weekdays",
    "weekdays": "time",
    "duration": "time",
    "temporal location": "time",
    "location": "property",
    "time": "property",
    "heading": "property",
    "manner": "property",
    "theology": "religion",
    "monotheism": "religion",
    "Catholicism": "Christianity",
    "Shinto": "religion",
    "Gnosticism": "religion",
    "Protestantism": "Christianity",
    "occultism": "religion",
    "buddhism": "religion",
    "hinduism": "religion",
    "Roman Catholicism": "Catholicism",
    "position": "location",
    "origin": "location",
    "source": "location",
    "cause": "property",
    "state": "property",
    "naturism": "lifestyle",
    "carnaval": "lifestyle",
    "organic chemistry": "chemistry",
    "inorganic chemistry": "chemistry",
    "gaming": "games",
    "SI units": "units-of-measure",
    "units of measure": "units-of-measure",
}
