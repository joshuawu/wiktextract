import unittest
from collections import defaultdict

from wikitextprocessor import Wtp

from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.de.example import extract_examples, extract_reference

from wiktextract.thesaurus import close_thesaurus_db
from wiktextract.wxr_context import WiktextractContext


class TestDEExample(unittest.TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.wxr = WiktextractContext(
            Wtp(lang_code="de"), WiktionaryConfig(dump_file_lang_code="de")
        )

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()
        close_thesaurus_db(
            self.wxr.thesaurus_db_path, self.wxr.thesaurus_db_conn
        )

    def test_de_extract_examples(self):
        self.wxr.wtp.start_page("")
        root = self.wxr.wtp.parse(
            ":[1] example1A \n:[1] example1B\n:[2] example2\n:[3] example3"
        )

        page_data = [defaultdict(list)]
        page_data[-1]["senses"] = [
            defaultdict(list, {"senseid": "1"}),
            defaultdict(list, {"senseid": "2"}),
        ]

        extract_examples(self.wxr, page_data, root.children[0])

        self.assertEqual(
            page_data,
            [
                {
                    "senses": [
                        {
                            "examples": [
                                {"text": "example1A"},
                                {"text": "example1B"},
                            ],
                            "senseid": "1",
                        },
                        {
                            "examples": [{"text": "example2"}],
                            "senseid": "2",
                        },
                    ]
                }
            ],
        )

    def test_de_extract_example_with_reference(self):
        self.wxr.wtp.start_page("")
        root = self.wxr.wtp.parse(":[1] example1 <ref>ref1A</ref>")

        page_data = [defaultdict(list)]
        page_data[-1]["senses"] = [
            defaultdict(list, {"senseid": "1"}),
        ]

        extract_examples(self.wxr, page_data, root.children[0])

        self.assertEqual(
            page_data,
            [
                {
                    "senses": [
                        {
                            "examples": [
                                {
                                    "text": "example1",
                                    "ref": {"raw_ref": "ref1A"},
                                },
                            ],
                            "senseid": "1",
                        },
                    ]
                }
            ],
        )

    def test_de_extract_reference(self):
        self.wxr.wtp.start_page("")
        self.wxr.wtp.add_page("Vorlage:Literatur", 10, "Expanded template")
        root = self.wxr.wtp.parse("<ref>{{Literatur|Titel=title}}</ref>")

        example_data = defaultdict(str)

        extract_reference(self.wxr, example_data, root.children[0])

        self.assertEqual(
            example_data,
            {"ref": {"raw_ref": "Expanded template", "titel": "title"}},
        )
