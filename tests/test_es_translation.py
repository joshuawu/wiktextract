import unittest

from wikitextprocessor import Wtp
from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.es.models import WordEntry
from wiktextract.extractor.es.translation import extract_translation
from wiktextract.wxr_context import WiktextractContext


class TestESTranslation(unittest.TestCase):
    def setUp(self) -> None:
        self.wxr = WiktextractContext(
            Wtp(lang_code="es"),
            WiktionaryConfig(dump_file_lang_code="es"),
        )

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()

    def get_default_page_data(self) -> list[WordEntry]:
        return [
            WordEntry(
                word="test",
                lang_code="es",
                lang="Language",
            )
        ]

    def test_es_extract_translation(self):
        # Test cases from https://es.wiktionary.org/wiki/Plantilla:t+
        test_cases = [
            {
                # https://es.wiktionary.org/wiki/calderón
                "input": "{{t+|ar|}}",
                "expected": [],
            },
            {
                "input": "{{t+|af|1|kat}}",
                "expected": [
                    {
                        "lang": "afrikáans",
                        "lang_code": "af",
                        "word": "kat",
                        "senseids": ["1"],
                    }
                ],
            },
            {
                "input": "{{t+|de|1, 2|Katze|f|,|1|Kater|m|nota|gato macho|,|8|Tic Tac Toe}}",
                "expected": [
                    {
                        "lang": "alemán",
                        "lang_code": "de",
                        "word": "Katze",
                        "senseids": ["1", "2"],
                        "raw_tags": ["f"],
                    },
                    {
                        "lang_code": "de",
                        "lang": "alemán",
                        "word": "Kater",
                        "senseids": ["1"],
                        "raw_tags": ["m"],
                        "notes": ["gato macho"],
                    },
                    {
                        "lang_code": "de",
                        "lang": "alemán",
                        "word": "Tic Tac Toe",
                        "senseids": ["8"],
                    },
                ],
            },
            {
                "input": "{{t+|fr|1|profession|nl|de|bateleur}}",
                "expected": [
                    {
                        "lang": "francés",
                        "lang_code": "fr",
                        "word": "profession de bateleur",
                        "senseids": ["1"],
                    }
                ],
            },
            {
                "input": "{{t+|hy|1|կատու|tr|katu}}",
                "expected": [
                    {
                        "lang": "armenio",
                        "lang_code": "hy",
                        "word": "կատու",
                        "roman": "katu",
                        "senseids": ["1"],
                    }
                ],
            },
            {
                "input": "{{t+|hy|1|կատու|tr=katu}}",
                "expected": [
                    {
                        "lang": "armenio",
                        "lang_code": "hy",
                        "word": "կատու",
                        "roman": "katu",
                        "senseids": ["1"],
                    }
                ],
            },
            {
                "input": "{{t+|de|amphibisch|adj|,|Amphibie|sust|,|Amphibium|sust}}",
                "expected": [
                    {
                        "lang": "alemán",
                        "lang_code": "de",
                        "word": "amphibisch",
                        "raw_tags": ["adj"],
                    },
                    {
                        "lang": "alemán",
                        "lang_code": "de",
                        "word": "Amphibie",
                        "raw_tags": ["sust"],
                    },
                    {
                        "lang": "alemán",
                        "lang_code": "de",
                        "word": "Amphibium",
                        "raw_tags": ["sust"],
                    },
                ],
            },
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.wxr.wtp.start_page("")
                page_data = self.get_default_page_data()

                root = self.wxr.wtp.parse(case["input"])

                extract_translation(self.wxr, page_data[-1], root.children[0])

                translations = [
                    t.model_dump(exclude_defaults=True)
                    for t in page_data[-1].translations
                ]
                self.assertEqual(
                    translations,
                    case["expected"],
                )
