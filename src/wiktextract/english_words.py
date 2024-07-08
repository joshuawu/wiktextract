# Vocabulary of known English words.
#
# The vocabulary is mostly based on ntlk brown corpus, but we add some words
# and exclude some words.  These will likely need to be tweaked semi-frequently
# to add support for unrecognized sense descriptions.
#
# Copyright (c) 2020-2022 Tatu Ylonen.  See file LICENSE and https://ylonen.org

import nltk  # type: ignore[import-untyped]
from nltk.corpus import brown  # type: ignore[import-untyped]

from .form_descriptions_known_firsts import known_firsts  # w/ our additions

# Download Brown corpus if not already downloaded
try:
    nltk.data.find("corpora/brown.zip")
except LookupError:
    nltk.download("brown", quiet=True)

# English words added to the default set from Brown corpus.  Multi-word
# expressions separated by spaces can also be added but must match the whole
# text (they can be used when we don't want to add the components).
additional_words = set(
    [
        "'",
        "ʹ",
        ".",
        ";",
        ":",
        "!",
        "‘",
        "’",
        '"',
        "“",
        "”",
        '"',
        ",",
        "…",
        "...",
        "“.”",
        "—",
        "€",
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "100th",
        "AIDS",
        "AM",
        "ATP",
        "Ada Semantic Interface Specification",
        "Afghanistan",
        "Al Jazeera",
        "Albulidae",
        "Apple",
        "Arabic kaf",
        "Arabic waw",
        "Aristophanean",
        "ASCII",
        "BBC",
        "BDSM",
        "BMW",
        "BS",
        "Bardet-Biedl syndrome",
        "Beetle",
        "Bekenstein-Hawking entropy",
        "Blu-ray",
        "Blu-ray Disc",
        "Bohai Sea",
        "Caniformia",
        "Canoidea",
        "Caprobrotus",
        "Chaetodontinae",
        "Common",
        "Compatibility Decomposition",
        "Coriandum",
        "Cryptodiran",
        "Czech",
        "DNA",
        "Dirac",
        "Dr",
        "Epiprocta",
        "Esau",
        "Eucharist",
        "Euclidean",
        "Exmoor",
        "Feliformia",
        "Feloidea",
        "GUI",
        "GameCube",
        "Global Positioning System",
        "Guantanamo",
        "Gurmukhi digits",
        "HCHO",
        "HMMWV",
        "HTTP",
        "Handedness",
        "Hearthstone",
        "Hollandic",
        "Horae",
        "Hue Whiteness Blackness",
        "I Ching hexagrams",
        "IPA",
        "ISO",
        "Indo",
        "Inoperable",
        "Internet",
        "Judeo",
        "LGBT",
        "Lagerstomia",
        "Latinized",
        "Linux",
        "Lunar Module",
        "Lyman continuum photon",
        "Mac",
        "Mach",
        "Markarian",
        "Masturbation",
        "Maulisa",
        "McDonald's",
        "Mercenaria",
        "Merseyside",
        "Metric",
        "Monetaria",
        "Mr",
        "Mr Spock",
        "Mrs",
        "Ms",
        "Mugillidae",
        "Multiples",
        "NCO",
        "Nepali",
        "New",
        "Nintendo",
        "Noh",
        "Numbers",
        "Nun",
        "Onchorhynchus",
        "Orgasm",
        "OS",
        "Palmaiola",
        "Pentecost",
        "Phoenician",
        "Plebidonax",
        "PM",
        "Pornography",
        "Prof",
        "Roma",
        "Romani",
        "Russian krai",
        "Russophile",
        "SARS",
        "SI",
        "Sandwich",
        "Saskatchewan",
        "Shahmukhi digits",
        "Silent Information Regulator",
        "Sony",
        "Southern",
        "Spanish-speaking",
        "THz",
        "Tamil digits",
        "Telugu digits",
        "Turkic",
        "Twitter",
        "UAV",
        "USB",
        "USD",
        "USSF",
        "Unicode",
        "Uranus",
        "Urdu digits",
        "Valais",
        "Volkswagen",
        "X-Files",
        "WC",
        "WW2",
        "Wallis",
        "Web",
        "Wi-Fi",
        "Windows",
        "World",
        "XML Paper Specification",
        "abbreviation",
        "abdicate",
        "abdication",
        "abhor",
        "abhorrence",
        "abnormality",
        "abiotic",
        "aboriginals",
        "aborted",
        "abouts",
        "abrasive",
        "abridging",
        "abscess",
        "absorbent",
        "abstinent",
        "abuser",
        "acanthesthesia",
        "accusatorial",
        "acetous",
        "acetylcarnitine",
        "acetylsalicylic",
        "acidic",
        "acne",
        "acorn",
        "acquiescent",
        "acrimonious",
        "acrimony",
        "acromegaly",
        "activist",
        "acyclic",
        "acyl",
        "addict",
        "addend",
        "adicity",
        "admonish",
        "adornment",
        "adpositions",
        "adulterer",
        "adulterous",
        "aeroplane",
        "affectedly",
        "affixes",
        "affordable",
        "afterthought",
        "agnathia",
        "agoraphobia",
        "agression",
        "aground",
        "airbag",
        "airtight",
        "ait",
        "albumen",
        "alchemist",
        "aldehyde",
        "aldohexose",
        "alga",
        "alimentary",
        "aliphatic",
        "allele",
        "allergen",
        "allergological",
        "alleyway",
        "allotrope",
        "allude",
        "almond",
        "alms",
        "alphabets",
        "alpine",
        "ambergris",
        "ammeter",
        "amoeba",
        "amorously",
        "amphetamine",
        "amphibian",
        "amphibole",
        "amputate",
        "anachronistic",
        "anaemia",
        "anaemic",
        "anal",
        "angiosperms",
        "angiotensin",
        "angled",
        "angler",
        "angleworm",
        "anglicism",
        "angstrom",
        "anilingus",
        "annealing",
        "annexation",
        "anno",
        "annoyingly",
        "annuity",
        "annul",
        "anoint",
        "ante",
        "antechamber",
        "anteroposterior",
        "anthill",
        "anti-doping",
        "anti-streptolysin",
        "anticlimax",
        "anticline",
        "anticlockwise",
        "antipyretic",
        "antisense",
        "antonym",
        "antonymous",
        "anus",
        "anxiogenic",
        "aortic",
        "apatite",
        "aphaeretic",
        "aphorisms",
        "apollonian",
        "apologue",
        "apostrophe",
        "applique",
        "appendage",
        "appendectomy",
        "appendicitis",
        "appentice",
        "appetising",
        "apprentice",
        "approvable",
        "aquarium",
        "aquatic",
        "arachnid",
        "archer",
        "argipalla",
        "arity",
        "armour",
        "armoured",
        "aromantic",
        "arse",
        "arsenolite",
        "artifact",
        "artwork",
        "asbestiform",
        "aspirate",
        "asscheek",
        "assuaging",
        "astrological",
        "atrium",
        "audiovisual",
        "averring",
        "avoirdupois",
        "babble",
        "backup",
        "bagpiper",
        "ballcourt",
        "ballgame",
        "ballpoint",
        "bamboo",
        "banality",
        "banknote",
        "barb",
        "barefaced",
        "barrister",
        "barter",
        "basset",
        "bathhouse",
        "batty",
        "bead",
        "beak",
        "begrudging",
        "belittle",
        "belladona",
        "benefice",
        "benzoyl",
        "bequeath",
        "berbicara",
        "bereave",
        "bereaved",
        "bestiality",
        "bianwen",
        "bidirectional",
        "bigwig",
        "bilberry",
        "birthmark",
        "blabs",
        "blackbird",
        "bladder",
        "blastula",
        "blockhead",
        "bloodworts",
        "blotches",
        "bluefin",
        "blurring",
        "bob",
        "bobbin",
        "bodyfat",
        "bogaraveo",
        "bollard",
        "bonsai",
        "bobsledding",
        "bookmaker",
        "bootleg",
        "boozy",
        "botcher",
        "bottomed",
        "boyfriend",
        "bra",
        "braid",
        "braking",
        "breakdancer",
        "breastplate",
        "breathalyzer",
        "bribery",
        "brier",
        "brimless",
        "brimming",
        "bristletail",
        "broadsword",
        "browse",
        "browser",
        "brutish",
        "bung",
        "burbot",
        "burti",
        "byte",
        "caesura",
        "caipira",
        "calcareous",
        "calculator",
        "camouflaging",
        "canal",
        "canard",
        "candensis",
        "canid",
        "cannabis",
        "canoer",
        "canoeist",
        "canton",
        "capercaillie",
        "caprice",
        "capriciously",
        "caption",
        "carbonate",
        "carbonated",
        "carex",
        "carnivoran",
        "carnivore",
        "carnivorous",
        "carpus",
        "cartilaginous",
        "cartload",
        "carucates",
        "cashier",
        "cassette",
        "cassia",
        "cassowary",
        "castellan",
        "castes",
        "castrated",
        "cataract",
        "catastrophist",
        "cation",
        "cauldron",
        "causer",
        "caustic",
        "cedar",
        "celluloid",
        "censoring",
        "centralised",
        "cerebropathy",
        "ceremonious",
        "cervical",
        "cetacean",
        "chainsaw",
        "chaste",
        "chastely",
        "chav",
        "cheeky",
        "cheerless",
        "cheetahs",
        "cheque",
        "chessman",
        "chesspiece",
        "chewable",
        "chlorofluorocarbon",
        "chopsticks",
        "chrysantemum",
        "churl",
        "cinnabar",
        "cinnamon",
        "circumcised",
        "circumvent",
        "citronella",
        "clade",
        "clamp",
        "clapper",
        "classifier",
        "cleanliness",
        "cleave",
        "clef",
        "clitoral",
        "clitoris",
        "cloister",
        "coatroom",
        "cobbled",
        "cockfighting",
        "coddle",
        "codlings",
        "codomain",
        "coenzyme",
        "cogwheel",
        "cohabit",
        "coinage",
        "collectivisation",
        "collide",
        "colour",
        "colourless",
        "columbium",
        "combinatorial",
        "commandery",
        "commemoration",
        "common linnet et al",
        "compasses",
        "complainer",
        "comprehensible",
        "conceit",
        "concha",
        "concubine",
        "condiment",
        "condom",
        "conductance",
        "confection",
        "conformable",
        "conforming",
        "congeal",
        "congealable",
        "congee",
        "conical",
        "conjuring",
        "connector",
        "consession",
        "console",
        "constable",
        "constellation",
        "contaminant",
        "contemn",
        "contort",
        "contractions",
        "coolie",
        "copula",
        "copular",
        "copulate",
        "copulation",
        "cornel",
        "cornucopiodes",
        "corvid",
        "cosmogony",
        "costermonger",
        "councillor",
        "counsellor",
        "countably",
        "counterintuitive",
        "countrified",
        "courier",
        "cowpat",
        "cowshed",
        "crabby",
        "cracker",
        "cranberry",
        "crayon",
        "creatine",
        "creatinine",
        "creditor",
        "cremation",
        "creole",
        "crewed",
        "cribbage",
        "cricketer",
        "cringe",
        "criticise",
        "croissant",
        "croquet",
        "crossbar",
        "crossbow",
        "crossword",
        "crosswords",
        "crumb",
        "crustacean",
        "crustaceans",
        "crybaby",
        "cuckoldry",
        "cuckoo",
        "cucumber",
        "cuirass",
        "cultivar",
        "culvert",
        "cum",
        "cursive",
        "curvaceous",
        "custard",
        "cutie",
        "cuttlefish",
        "cutlery",
        "cybernetics",
        "cycling",
        "cyclone",
        "cypro",
        "cytopharynx",
        "dab",
        "daimyo",
        "daresay",
        "darken",
        "dart",
        "dawdle",
        "daydream",
        "deaconship",
        "debased",
        "debit",
        "decaffeinated",
        "decapod",
        "deceitfulness",
        "decipher",
        "deciphered",
        "decoction",
        "defamatory",
        "defame",
        "defecation",
        "defile",
        "definiteness",
        "degenerate",
        "dehusking",
        "deifying",
        "deity",
        "dejected",
        "deleted",
        "deltoidal",
        "dementia",
        "demo",
        "demolish",
        "demonym",
        "denim",
        "denture",
        "deponent",
        "depressed",
        "derisorily",
        "designator",
        "desorption",
        "despicable",
        "detent",
        "dexterous",
        "diacritics",
        "diaeresis",
        "diaper",
        "dictionaries",
        "digressing",
        "digust",
        "dike",
        "dimness",
        "diplomatique",
        "dipterous",
        "disadvantageous",
        "disallow",
        "disavow",
        "discoloured",
        "disconnect",
        "disconnection",
        "discrepant",
        "disembark",
        "dishonour",
        "dispensable",
        "dispirited",
        "displeasing",
        "disputatively",
        "disrespectful",
        "diss",
        "dissipatedisyllabicity",
        "distaff",
        "disulfide",
        "doer",
        "dogfight",
        "dogfish",
        "domesticated",
        "doorhandle",
        "doorpost",
        "dorsal",
        "dotard",
        "doughnut",
        "download",
        "downmarket",
        "doyen",
        "dreadlock",
        "dreadlocks",
        "dredge",
        "duckling",
        "dude",
        "dull-witted",
        "dunce",
        "dupe",
        "duplicating",
        "duplicity",
        "dye",
        "dyes",
        "dyestuff",
        "eater",
        "eavesdrop",
        "echinoderms",
        "eclectic",
        "ecosystem",
        "ecstacy",
        "ectoderm",
        "effervescing",
        "egregious",
        "eigenvector",
        "ejaculate",
        "ejaculation",
        "electromechanical",
        "electroplate",
        "elephantiasis",
        "em dash",
        "emaciation",
        "email",
        "emoticon",
        "encasing",
        "encephalomyelitis",
        "enclitic",
        "enclose",
        "endocrine",
        "enforcer",
        "engrave",
        "engross",
        "enliven",
        "enquire",
        "entangle",
        "entangled",
        "entice",
        "entitlement",
        "entrails",
        "entrenchment",
        "enumerate",
        "enumerating",
        "envelops",
        "epichoric",
        "epilepsy",
        "epistle",
        "equinox",
        "esophagus",
        "espresso",
        "estrange",
        "etc",
        "etching",
        "ethane",
        "ethnicity",
        "ethology",
        "ethylene",
        "euro",
        "euthanize",
        "evergreen",
        "exaction",
        "exam",
        "exclesior",
        "excommunication",
        "excrement",
        "excrete",
        "excretement",
        "exhale",
        "exhort",
        "exine",
        "explainable",
        "expletive",
        "extortion",
        "extravagantly",
        "extraverted",
        "eyelet",
        "factious",
        "faeces",
        "faggot",
        "fairground",
        "falsely",
        "fandom",
        "fanfiction",
        "fart",
        "farthing",
        "fastener",
        "feces",
        "feigns",
        "feline",
        "felines",
        "fellatio",
        "fellator",
        "feminin",
        "fend",
        "feng",
        "feng shui",
        "fengshui",
        "feral",
        "fester",
        "fetter",
        "fewness",
        "fiancé",
        "fiancée",
        "fibre",
        "figuratively",
        "filches",
        "filching",
        "fillet",
        "fillets",
        "filterer",
        "filtration",
        "finalise",
        "firearm",
        "firebreak",
        "firefighter",
        "fireside",
        "firmware",
        "fishnet",
        "fishy",
        "fissure",
        "flatbed",
        "flattish",
        "flavour",
        "flea",
        "flightless",
        "foehn",
        "fondle",
        "footprint",
        "footrest",
        "fop",
        "forcefully",
        "ford",
        "foreshow",
        "fossil",
        "fraternal",
        "fratricide",
        "fraudulent",
        "fraudulently",
        "fredag",
        "freemasonic",
        "freestyle",
        "frequentative",
        "freshwater",
        "fridge",
        "frigate",
        "frisson",
        "fritter",
        "frontflip",
        "frontotemporal",
        "frugal",
        "fulfilment",
        "fumigating",
        "functionality",
        "fundoshi",
        "furry",
        "furthest",
        "gadoid",
        "gameplay",
        "gamling",
        "gastropod",
        "gatepost",
        "gelatinous",
        "gemstone",
        "genderqueer",
        "genealogy",
        "generative",
        "generic",
        "generically",
        "genericized",
        "genital",
        "genitalia",
        "genitals",
        "genitourinary",
        "genus",
        "geometrid",
        "getter",
        "ghostwriter",
        "giga-",
        "giraffe",
        "girder",
        "girlfriend",
        "ginseng",
        "gizzard",
        "glans",
        "glassworks",
        "glowworm",
        "glutton",
        "glycoside",
        "goalkeeper",
        "goalpost",
        "gobble",
        "goby-like",
        "god-given",
        "goddesses",
        "gonad",
        "goodwill",
        "gorged",
        "gouge",
        "graceless",
        "grafting",
        "grandchild",
        "gratuity",
        "gravedigger",
        "grebe",
        "grid",
        "grouch",
        "groupers",
        "grouse",
        "guarantor",
        "guilder",
        "guillotine",
        "guitarfish",
        "guillemets",
        "habitation",
        "habitational",
        "hagberry",
        "hairstyle",
        "hamster",
        "handball",
        "harbinger",
        "hardcore",
        "harmonize",
        "harvester",
        "harvesters",
        "hashish",
        "hassock",
        "hatefully",
        "hawksbill",
        "hawthorn",
        "hayfield",
        "hazarded",
        "headlight",
        "headlong",
        "heaths",
        "hemp",
        "heraldic",
        "heraldry",
        "herbal",
        "heterosexual",
        "hi",
        "hieroglyphs",
        "hilted",
        "hip-hop",
        "hircinous",
        "hives",
        "hoarfrost",
        "hoariness",
        "hoe",
        "holiness",
        "holly",
        "homeless",
        "homie",
        "homosexuality",
        "honorific",
        "hornet",
        "horny",
        "horseshoe",
        "horticultural",
        "hostel",
        "houseboat",
        "howin",
        "hulled",
        "humiliate",
        "humour",
        "hump",
        "husked",
        "hydroxylase",
        "hyperactivity",
        "hyperlink",
        "hypersensitivity",
        "hypersonic",
        "hyphen",
        "ichthyological",
        "icon",
        "icositetrahedron",
        "ignoble",
        "ikebana",
        "illicitly",
        "illiteracy",
        "imaginable",
        "immaturely",
        "immerse",
        "immune",
        "impermeable",
        "impiously",
        "impregnate",
        "imprison",
        "impure",
        "in-law",
        "inappropriately",
        "incredulousness",
        "incriminate",
        "indefinably",
        "indentation",
        "indistinguishably",
        "ineptitude",
        "infatuated",
        "inflectional",
        "informer",
        "infraclass",
        "infrakingdom",
        "infraorder",
        "infraphylum",
        "ingesting",
        "inhabitant",
        "inhabiting",
        "inhale",
        "injure",
        "inlaying",
        "innapropriate",
        "inoffensive",
        "inoperable",
        "inoperative",
        "inscribe",
        "insinuate",
        "inspan",
        "instrumentalist",
        "intenseness",
        "intoxication",
        "intoxification",
        "inventiveness",
        "irascible",
        "irritate",
        "islamic",
        "islet",
        "isotope",
        "jack",
        "javelin",
        "jellyfish",
        "jerkily",
        "jokingly",
        "junket",
        "kaf",
        "kangaroo",
        "kanji",
        "katydid",
        "kayak",
        "kestrel",
        "ketamine",
        "kidskin",
        "killjoy",
        "kilo-",
        "kilt",
        "kinase",
        "kingfisher",
        "kitsch",
        "kiwi",
        "knighthood",
        "kookaburra",
        "kowtow",
        "kroepoek",
        "kung fu",
        "labial",
        "labour",
        "lair",
        "lamprey",
        "lampshade",
        "landmass",
        "landmasses",
        "laptop",
        "larch",
        "larva",
        "lascivious",
        "latte",
        "lattice",
        "laughable",
        "leafless",
        "lecherous",
        "leech",
        "leek",
        "leftover",
        "legless",
        "lemming",
        "leniusculus",
        "leotard",
        "lesbian",
        "lettuce",
        "lexeme",
        "lichen",
        "lifespan",
        "ligature",
        "lighthouse",
        "lily",
        "litre",
        "little sis",
        "lizard",
        "loanword",
        "loggerhead",
        "loiter",
        "longline",
        "loofah",
        "lottery",
        "lowercase",
        "ludifica",
        "luxuriant",
        "lye",
        "madder",
        "mafia",
        "magnanimous",
        "magnetite",
        "magnorder",
        "manageable",
        "mangoes",
        "manna",
        "manoeuvre",
        "manroot",
        "maqaf",
        "marmot",
        "marsh",
        "marshy",
        "marsupial",
        "masturbate",
        "masturbates",
        "masturbating",
        "masturbation",
        "masturbator",
        "materialise",
        "matra",
        "mayfly",
        "mead",
        "meagre",
        "mediates",
        "mediator",
        "mega-",
        "megalitre",
        "melanin",
        "meningitis",
        "menorah",
        "menstrual",
        "meow",
        "mercenaria",
        "mercenary",
        "meridiem",
        "mesmerism",
        "metalworks",
        "metamphetamine",
        "methamphetamine",
        "methane",
        "metric",
        "microcomputer",
        "microprocessor",
        "midbrain",
        "milkman",
        "millet",
        "millstone",
        "minifig",
        "minifigure",
        "minting",
        "minuscules",
        "mire",
        "misbehave",
        "miscarriage",
        "miserly",
        "mislead",
        "misspelling",
        "misspelt",
        "mite",
        "mitral stenosis",
        "modem",
        "module",
        "modulus",
        "mollusc",
        "mollusk",
        "mongrel",
        "monogram",
        "monopolizing",
        "monosemy",
        "monosilane",
        "monotheistic",
        "moonshine",
        "moralization",
        "morel",
        "motorcycle",
        "motorsport",
        "motorsports",
        "moult",
        "mourner",
        "mouselike",
        "mouthpart",
        "mow",
        "muddle",
        "mugwort",
        "mulberry",
        "multiplier",
        "muntjac",
        "mutation",
        "myalgic",
        "mythical",
        "nags",
        "nape",
        "narrate",
        "naturopathic",
        "naughtily",
        "nave",
        "neighbour",
        "nerd",
        "nescio",
        "networking",
        "neume",
        "neurotransmitter",
        "newsflash",
        "nictinic",
        "nightjar",
        "nimble",
        "ninjutsu",
        "niobium",
        "nipple",
        "nitric",
        "nitrite",
        "noh",
        "noice",
        "nomen",
        "non-Roma",
        "nonchalance",
        "nonessential",
        "nonfatal",
        "nonstandard",
        "nontrivial",
        "nonzero",
        "noodles",
        "normality",
        "nosocomial",
        "notionally",
        "nucleon",
        "numeral",
        "numeric",
        "nuqta",
        "oar",
        "oars",
        "obese",
        "oblast",
        "obligatory",
        "obnoxiously",
        "obtuse",
        "octahedral",
        "octave",
        "odour",
        "oligonucleotide",
        "om",
        "omnivorous",
        "onerous",
        "online",
        "oppress",
        "ore",
        "organinc",
        "organisation",
        "oscillate",
        "osier",
        "osmanthus",
        "ostmanthus",
        "otolaryngology",
        "ouch",
        "outergarment",
        "outtake",
        "ouzel",
        "overseeing",
        "overshoe",
        "overstate",
        "overstep",
        "overused",
        "ovum",
        "oxgang",
        "paddle",
        "paenungulates",
        "palatalized",
        "palmistry",
        "paltry",
        "pancake",
        "pancakes",
        "pantherine",
        "papules",
        "paralysed",
        "paraphrasis",
        "parenthetical",
        "parere",
        "parietal",
        "paronomasia",
        "participle",
        "parvorder",
        "pasta",
        "pastern",
        "patchy",
        "paternal",
        "patty",
        "pawl",
        "pawpaw",
        "pedant",
        "pediment",
        "peevish",
        "peloton",
        "pelt",
        "penetrable",
        "penguin",
        "penile",
        "penis",
        "penitent",
        "pentatonic",
        "perceivable",
        "perceptiveness",
        "perfluorooctanoic",
        "perineum",
        "perjurer",
        "peroxidase",
        "perspire",
        "pervert",
        "pessimist",
        "petal",
        "petrel",
        "petrol",
        "pewter",
        "phenylalanine",
        "phobia",
        "phoneme",
        "photocopier",
        "photocopy",
        "photosynthetic",
        "phthisic",
        "phthisical",
        "phylogenetics",
        "phylum",
        "pickpocket",
        "piddle",
        "piecework",
        "pierce",
        "pigmentation",
        "pilfered",
        "pinecone",
        "pinewood",
        "pistil",
        "pixelization",
        "placable",
        "placeholder",
        "placenta",
        "plantlike",
        "playlist",
        "pleasurable",
        "plectrum",
        "plinth",
        "ploughgate",
        "ploughgates",
        "plunderer",
        "plural",
        "pointy",
        "pokeweed",
        "pollute",
        "polycyclic",
        "polyglot",
        "polygon",
        "polyhedra",
        "polyhedron",
        "polyiamond",
        "polytheistic",
        "polytope",
        "polyurethane",
        "pomelo",
        "pommel",
        "pons",
        "ponyfish",
        "popcorn",
        "portend",
        "positiveness",
        "possibly",
        "posteroanterior",
        "postposition",
        "postpositional",
        "potable",
        "prawn",
        "precipitous",
        "predatory",
        "predicative",
        "prefix",
        "premeditated",
        "preservative",
        "preternatural",
        "primrose",
        "prismatic",
        "proclitic",
        "procreate",
        "profanities",
        "prolapse",
        "promiscuous",
        "pronated",
        "prong",
        "pronunciation",
        "proofreading",
        "prosthetic",
        "protector",
        "prothrombin",
        "protists",
        "proto",
        "protracting",
        "provident",
        "provider",
        "provocativeness",
        "provoking",
        "psychometrics",
        "psychopathological",
        "pubic",
        "pudding",
        "puffin",
        "purloin",
        "purr",
        "pushchair",
        "pushy",
        "pyrotechnic",
        "quad",
        "quadrilateral",
        "quahog",
        "quantifying",
        "quark",
        "queue",
        "quiche",
        "quietude",
        "quilt",
        "quiver",
        "radiotherapy",
        "ramie",
        "rapids",
        "raptors",
        "rashly",
        "raven",
        "ravenously",
        "ravine",
        "reactive",
        "readied",
        "realtime",
        "redskin",
        "redstart",
        "reed",
        "reentry",
        "reeve",
        "refinedly",
        "refiner",
        "reflexive",
        "reflexively",
        "refutation",
        "regardful",
        "regnant",
        "regressive",
        "reindeer",
        "reintegrationist",
        "reinvigorated",
        "relenting",
        "relinquishment",
        "remiss",
        "renounce",
        "reordered",
        "repairer",
        "reprimand",
        "reproductory",
        "reptile",
        "republican",
        "reset",
        "restroom",
        "retract",
        "retread",
        "reunification",
        "reusable",
        "reveler",
        "revengefully",
        "rhetorical",
        "rhinarium",
        "rhombus",
        "rhotic",
        "rhubarb",
        "ribavirin",
        "riffraff",
        "ripen",
        "riverbed",
        "roasting",
        "rockhopper",
        "roe",
        "roman",
        "romanisation",
        "romanization",
        "rook",
        "roundel",
        "rout",
        "rudiments",
        "rugby",
        "rumination",
        "rummage",
        "saman",
        "samurai",
        "sandbank",
        "satirize",
        "saucer",
        "sautéed",
        "saveloy",
        "savoury",
        "sawfly",
        "sawhorse",
        "scabby",
        "scabs",
        "scaleless",
        "scampi",
        "scarecrow",
        "schoolbag",
        "scoff",
        "scoffs",
        "scold",
        "scraper",
        "screwdriver",
        "scribal",
        "scroll",
        "scrotum",
        "scuba",
        "scurf",
        "scythe",
        "seabird",
        "seaduck",
        "seagull",
        "seaplane",
        "seaport",
        "seemly",
        "seer",
        "selfishly",
        "selfsame",
        "semen",
        "semiconductor",
        "semimetal",
        "semipermeable",
        "senso",
        "sentimental",
        "separator",
        "sepulchring",
        "sequentially",
        "shamelessly",
        "shamisen",
        "shaojiu",
        "shark",
        "sheepfold",
        "shifter",
        "shindig",
        "shitting",
        "shoal",
        "shoemaker",
        "shoemaking",
        "shoeshine",
        "shuffleboard",
        "shuttlecock",
        "sibling",
        "siblings",
        "sickbed",
        "sideband",
        "sidespin",
        "silkworm",
        "silt",
        "silverfish",
        "skateboard",
        "skein",
        "skerry",
        "skier",
        "sled",
        "sleeved",
        "sleeveless",
        "sloth",
        "slut",
        "slutty",
        "smegma",
        "sob",
        "sodomite",
        "software",
        "solfège",
        "solicitation",
        "sorcerer",
        "sorceress",
        "sororal",
        "spaceflight",
        "spacetime",
        "spadix",
        "spar",
        "sparingly",
        "sparrow",
        "spasmodic",
        "specesi",
        "speciality",
        "spellings",
        "sperm",
        "spiderweb",
        "spirally",
        "spiro",
        "spiteful",
        "spitefully",
        "splint",
        "spool",
        "spore",
        "spotnape",
        "spp",  # Commonly used abbreviation "spp."
                # for subspecies in species names
        "sprinkles",
        "sprite",
        "spritsail",
        "spruiks",
        "squander",
        "squeegee",
        "squid",
        "squint",
        "stabbing",
        "stalk",
        "stamen",
        "standalone",
        "starthistle",
        "steadfast",
        "steadfastness",
        "stealthy",
        "stenosis",
        "sth",
        "sthg",
        "stich",
        "sticker",
        "stinginess",
        "stinks",
        "stockaded",
        "stomachache",
        "stonechat",
        "storey",
        "stork",
        "stowaway",
        "straightness",
        "stricto",
        "strident",
        "stupefy",
        "subalgebra",
        "subbranch",
        "subclass",
        "subfamily",
        "subgenre",
        "subgenus",
        "subgroup",
        "subkingdom",
        "sublimely",
        "submatrix",
        "submerge",
        "suborder",
        "subphylum",
        "subscriber",
        "subsesquiplicate",
        "subset",
        "subsets",
        "subsonic",
        "substance",
        "subtribe",
        "succinctness",
        "sudoku",
        "sulk",
        "sumo",
        "sundial",
        "sunflower",
        "sunglasses",
        "sunshade",
        "sunshower",
        "superannuated",
        "supercharger",
        "superclass",
        "supercluster",
        "superdivision",
        "superdivisions",
        "superfamily",
        "superkingdom",
        "superorder",
        "superphylum",
        "supersede",
        "superunit",
        "surpassingly",
        "sustainer",
        "sutra",
        "swag",
        "swearword",
        "sweetener",
        "sweetening",
        "swimmer",
        "swimwear",
        "swindle",
        "swindler",
        "swoon",
        "swordfish",
        "symbiotic",
        "synaeresis",
        "syncope",
        "syperphylum",
        "systematics",
        "tableware",
        "tadpole",
        "tailcoat",
        "tallness",
        "tampon",
        "tanker",
        "tare",
        "tartrazine",
        "tastelessly",
        "tattle",
        "tattletale",
        "tattoo",
        "taxon",
        "taxonomic",
        "taxonomy",
        "tearful",
        "telecom",
        "telecommunication",
        "teller",
        "tera-",
        "tern",
        "terrene",
        "teshuva",
        "tesseract",
        "testicles",
        "tetrafluoromethane",
        "tetrafluoromonosilane",
        "tetragrams",
        "tetrahedron",
        "thorax",
        "thrombocytopenic",
        "thrombotic",
        "thunderstorm",
        "tibia",
        "tiddlywinks",
        "tieute",
        "tithe",
        "toady",
        "tofore",
        "tomography",
        "toothed",
        "topological",
        "topology",
        "torturer",
        "touchable",
        "towpath",
        "trainee",
        "tram",
        "trans",
        "transfinite",
        "transliteration",
        "transonic",
        "treachery",
        "tremulous",
        "trendy",
        "trepidation",
        "trickery",
        "triterpenoid",
        "trove",
        "trowelling",
        "truncations",
        "tsardom",
        "tuber",
        "tugboat",
        "tuna",
        "turmeric",
        "turner",
        "turnip",
        "tutelary",
        "twig",
        "twine",
        "two-up",
        "typeset",
        "typographer",
        "tyre",
        "unanswerable",
        "unassuming",
        "uncaring",
        "unchallenging",
        "unchaste",
        "uncircumcised",
        "uncivilised",
        "uncivilized",
        "uncomplicated",
        "unconventionally",
        "uncooked",
        "uncouth",
        "uncut",
        "undecided",
        "undergarment",
        "underpants",
        "understudy",
        "undulate",
        "undulation",
        "unevenly",
        "unfashionable",
        "unfasten",
        "unfavourable",
        "unfrequented",
        "ungulate",
        "unholy",
        "uninformed",
        "unintelligent",
        "unlikable",
        "unmoving",
        "unpeeled",
        "unprocessed",
        "unproven",
        "unraveling",
        "unravelled",
        "unravelling",
        "unrestrained",
        "unroll",
        "unscrupulously",
        "unsolicited",
        "unsorted",
        "unsound",
        "unspecialized",
        "unspecific",
        "untamed",
        "untried",
        "ununtrium",
        "unveiling",
        "unwell",
        "unworried",
        "uppercase",
        "urchin",
        "urinate",
        "urination",
        "usance",
        "utensil",
        "uterus",
        "vacating",
        "vacillate",
        "vandalize",
        "vane",
        "vapour",
        "var.",
        "variants",
        "verbose",
        "verlan",
        "verso",
        "vertebra",
        "vesicle",
        "vespers",
        "vibrance",
        "vibrate",
        "videotaped",
        "vim",
        "viol",
        "viper",
        "visor",
        "vitae",
        "voiceless",
        "voluptuary",
        "vomit",
        "voracious",
        "vulva",
        "wading",
        "wafer",
        "walkway",
        "wank",
        "wanker",
        "wantonly",
        "washerwoman",
        "watcher",
        "watchfulness",
        "watchman",
        "waterbirds",
        "watercraft",
        "waterlilies",
        "waw",
        "weaverbird",
        "webpage",
        "weevil",
        "wend",
        "wether",
        "whale",
        "whales",
        "whirlpool",
        "whitefish",
        "whitethorn",
        "whorl",
        "wildcard",
        "wildcat",
        "wildfire",
        "wimp",
        "windlass",
        "windpipe",
        "windscreen",
        "windward",
        "winemaking",
        "winterberry",
        "wisent",
        "womanlike",
        "woody",
        "workmate",
        "workplace",
        "worldliness",
        "worshipers",
        "worshipper",
        "wow",
        "wrasse",
        "wrench",
        "wrestler",
        "wrinkly",
        "yam",
        "yardland",
        "yarmulke",
        "youthfulness",
        "yuan",
        "zealotry",
        "zoospores",
        "zygosperm",
        "chamomile",
        "peppermint",
        "x-axis",
        "y-axis",
        "z-axis",
        "maté",
        "Wikimedia",
        "Wikipedia",
        "Wiktionary",
        "jargon",
    ]
)

# These words will never be treated as English words (overriding other
# considerations, not just membership in the set)
not_english_words_1 = set(
    [
        # This is a blacklist - these will not be treated as English words
        # even though they are in brown.words().  Adding a word on this list
        # generally makes it likely to be treated as a romanization.
        "ANU",
        "Franc",
        "Frans",
        "Germani",
        "Germania",
        "J'habitais",
        "Kina",
        "Mal",
        "Mi",
        "Mihapjungguk",
        "al",
        "avec",
        "boo",
        "de",
        "du",
        "em",
        "lui",
        "ma",
        "mana",
        "novo",
        "pronto",
        "que",
    ]
)

potentially_english_words = set(
    [
        "He",
        "Ye",
    ]
)

not_english_words = not_english_words_1 | potentially_english_words

# Construct a set of (most) English words.  Multi-word expressions where we
# do not want to include the components can also be put here space-separated.
english_words = (
    set(brown.words())
    | known_firsts
    |
    # XXX the second words of species names add too much garbage
    # now that we accept "english" more loosely.
    # set(x for name in known_species for x in name.split()) |
    additional_words
) - not_english_words
