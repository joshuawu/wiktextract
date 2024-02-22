from wiktextract.config import POSSubtitleData

# some are template names
POS_TITLES: POSSubtitleData = {
    "abreviatura": {"pos": "abbrev"},
    "acrónimo": {"pos": "abbrev"},
    "adjetivo cardinal": {"pos": "num"},
    "adjetivo demostrativo": {"pos": "adj"},
    "adjetivo indefinido": {"pos": "adj"},
    "adjetivo indeterminado": {"pos": "adj"},
    "adjetivo interrogativo": {"pos": "adj"},
    "adjetivo numeral": {"pos": "num"},
    "adjetivo ordinal": {"pos": "num"},
    "adjetivo posesivo": {"pos": "adj"},
    "adjetivo relativo": {"pos": "adj"},
    "adjetivo": {"pos": "adj"},
    "adverbio comparativo": {"pos": "adv"},
    "adverbio de afirmación": {"pos": "adv"},
    "adverbio de cantidad": {"pos": "adv"},
    "adverbio de duda": {"pos": "adv"},
    "adverbio de lugar": {"pos": "adv"},
    "adverbio de modo": {"pos": "adv"},
    "adverbio de negación": {"pos": "adv"},
    "adverbio de orden": {"pos": "adv"},
    "adverbio de tiempo": {"pos": "adv"},
    "adverbio demostrativo": {"pos": "adv"},
    "adverbio interrogativo": {"pos": "adv"},
    "adverbio relativo": {"pos": "adv"},
    "adverbio": {"pos": "adv"},
    "afijo": {"pos": "affix"},
    "artículo determinado": {"pos": "article"},
    "artículo indeterminado": {"pos": "article"},
    "artículo": {"pos": "article"},
    "circunfijo": {"pos": "circumfix"},
    "conjunción adversativa": {"pos": "conj"},
    "conjunción ilativa": {"pos": "conj"},
    "conjunción": {"pos": "conj"},
    "dígrafo": {"pos": "character"},
    "expresión": {"pos": "phrase"},
    "forma adjetiva": {"pos": "adj"},
    "forma de participio": {"pos": "participle"},
    "forma de sufijo": {"pos": "suffix"},
    "forma pronominal": {"pos": "pron"},
    "forma sustantiva femenina": {"pos": "noun"},
    "forma sustantiva masculina": {"pos": "noun"},
    "forma sustantiva neutra": {"pos": "noun"},
    "forma sustantiva": {"pos": "noun"},
    "forma verbal": {"pos": "verb"},
    "interjección": {"pos": "intj"},
    "letra": {"pos": "character"},
    "locución adjetiva": {"pos": "phrase"},
    "locución adverbial": {"pos": "phrase"},
    "locución conjuntiva": {"pos": "phrase"},
    "locución interjectiva": {"pos": "phrase"},
    "locución prepositiva": {"pos": "phrase"},
    "locución pronominal": {"pos": "phrase"},
    "locución sustantiva": {"pos": "phrase"},
    "locución verbal": {"pos": "phrase"},
    "locución": {"pos": "phrase"},
    "onomatopeya": {"pos": "noun"},
    "partícula": {"pos": "particle"},
    "postposición": {"pos": "postp"},
    "prefijo": {"pos": "prefix"},
    "preposición de ablativo": {"pos": "prep"},
    "preposición de acusativo o ablativo": {"pos": "prep"},
    "preposición de acusativo": {"pos": "prep"},
    "preposición de genitivo": {"pos": "prep"},
    "preposición": {"pos": "prep"},
    "pronombre demostrativo": {"pos": "pron"},
    "pronombre indefinido": {"pos": "pron"},
    "pronombre interrogativo": {"pos": "pron"},
    "pronombre personal": {"pos": "pron"},
    "pronombre posesivo": {"pos": "det"},
    "pronombre relativo": {"pos": "pron"},
    "pronombre": {"pos": "pron"},
    "refrán": {"pos": "proverb"},
    "sigla": {"pos": "abbrev"},
    "símbolo": {"pos": "symbol"},
    "sufijo flexivo": {"pos": "suffix"},
    "sufijo": {"pos": "suffix"},
    "sustantivo ambiguo": {"pos": "noun"},
    "sustantivo animado": {"pos": "noun"},
    "sustantivo común": {"pos": "noun"},
    "sustantivo femenino y masculino": {"pos": "noun"},
    "sustantivo femenino": {"pos": "noun"},
    "sustantivo inanimado": {"pos": "noun"},
    "sustantivo masculino": {"pos": "noun"},
    "sustantivo neutro y masculino": {"pos": "noun"},
    "sustantivo neutro": {"pos": "noun"},
    "sustantivo propio": {"pos": "name"},
    "sustantivo propio/pruebas": {"pos": "name"},
    "sustantivo": {"pos": "noun"},
    "verbo auxiliar": {"pos": "verb"},
    "verbo impersonal": {"pos": "verb"},
    "verbo intransitivo": {"pos": "verb"},
    "verbo modal": {"pos": "verb"},
    "verbo perfectivo": {"pos": "verb"},
    "verbo pronominal": {"pos": "verb"},
    "verbo transitivo": {"pos": "verb"},
    "verbo": {"pos": "verb"},
}

LINKAGE_TITLES: dict[str, str] = {
    "antónimo": "antonyms",
    "compuestos": "compounds",
    "derivad": "derived",
    "hipónimo": "hyponyms",
    "hiperónimo": "hypernyms",
    "merónimo": "meronyms",
    "locucion": "idioms",
    "locuciones": "idioms",
    "relacionado": "related",
    "refranes": "proverbs",
    "sinónimo": "synonyms",
}
