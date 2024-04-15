import unittest
from typing import List

from wikitextprocessor import Wtp
from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.es.gloss import (
    extract_gloss,
    process_ambito_template,
    process_uso_template,
)
from wiktextract.extractor.es.models import Sense, WordEntry
from wiktextract.wxr_context import WiktextractContext


class TestESGloss(unittest.TestCase):
    def setUp(self) -> None:
        self.wxr = WiktextractContext(
            Wtp(lang_code="es"),
            WiktionaryConfig(dump_file_lang_code="es"),
        )

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()

    def get_default_page_data(self) -> List[WordEntry]:
        return [WordEntry(word="test", lang_code="es", lang="Language")]

    def test_es_extract_glosses(self):
        # https://es.wiktionary.org/wiki/ayudar

        self.wxr.wtp.add_page("Plantilla:plm", 10, "Contribuir")
        self.wxr.wtp.start_page("")

        root = self.wxr.wtp.parse(
            """;1: {{plm|contribuir}} [[esfuerzo]] o [[recurso]]s para la [[realización]] de algo.
;2: Por antonomasia, [[cooperar]] a que alguno [[salir|salga]] de una [[situación]] [[dificultoso|dificultosa]]"""
        )

        page_data = self.get_default_page_data()

        extract_gloss(self.wxr, page_data, root.children[0])

        self.assertEqual(
            page_data[0].model_dump(exclude_defaults=True)["senses"],
            [
                {
                    "glosses": [
                        "Contribuir esfuerzo o recursos para la realización de algo."
                    ],
                    "senseid": "1",
                },
                {
                    "glosses": [
                        "Por antonomasia, cooperar a que alguno salga de una situación dificultosa"
                    ],
                    "senseid": "2",
                },
            ],
        )

    def test_es_extract_gloss_categories(self):
        # https://es.wiktionary.org/wiki/amor
        self.wxr.wtp.add_page("Plantilla:plm", 10, "Sentimiento")
        self.wxr.wtp.add_page(
            "Plantilla:sentimientos",
            10,
            "Humanidades. [[Categoría:ES:Sentimientos]]",
        )
        self.wxr.wtp.start_page("")

        root = self.wxr.wtp.parse(
            ";1 {{sentimientos}}: {{plm|sentimiento}} [[afectivo]] de [[atracción]], [[unión]] y [[afinidad]] que se experimenta hacia una persona, animal o cosa"
        )

        page_data = self.get_default_page_data()

        extract_gloss(self.wxr, page_data, root.children[0])

        self.assertEqual(
            page_data[0].model_dump(exclude_defaults=True)["senses"],
            [
                {
                    "glosses": [
                        "Sentimiento afectivo de atracción, unión y afinidad que se experimenta hacia una persona, animal o cosa"
                    ],
                    "senseid": "1",
                    "raw_tags": ["Humanidades"],
                    "categories": ["ES:Sentimientos"],
                }
            ],
        )

    def test_gloss_topics(self):
        self.wxr.wtp.start_page("helicóptero")
        self.wxr.wtp.add_page(
            "Plantilla:csem",
            10,
            "Aeronáutica, vehículos[[Categoría:ES:Aeronáutica|HELICOPTERO]][[Categoría:ES:Vehículos|HELICOPTERO]]",
        )
        page_data = [
            WordEntry(lang_code="es", lang="Español", word="helicóptero")
        ]
        root = self.wxr.wtp.parse(
            ";1 {{csem|aeronáutica|vehículos}}: Vehículo para desplazarse por el aire"
        )
        extract_gloss(self.wxr, page_data, root.children[0])
        self.assertEqual(
            page_data[0].model_dump(exclude_defaults=True)["senses"],
            [
                {
                    "glosses": ["Vehículo para desplazarse por el aire"],
                    "senseid": "1",
                    "topics": ["aeronautics", "vehicles"],
                    "categories": ["ES:Aeronáutica", "ES:Vehículos"],
                }
            ],
        )

    def test_uso_template(self):
        self.wxr.wtp.start_page("domingo")
        sense = Sense()
        self.wxr.wtp.add_page(
            "Plantilla:uso",
            10,
            ":*'''Uso:''' coloquial, despectivo[[Categoría:ES:Términos coloquiales|DOMINGO]][[Categoría:ES:Términos despectivos|DOMINGO]]",
        )
        root = self.wxr.wtp.parse("{{uso|coloquial|despectivo}}")
        process_uso_template(self.wxr, sense, root.children[0])
        self.assertEqual(
            sense.model_dump(exclude_defaults=True),
            {
                "categories": [
                    "ES:Términos coloquiales",
                    "ES:Términos despectivos",
                ],
                "tags": ["colloquial", "derogatory"],
            },
        )

    def test_ambito_template(self):
        self.wxr.wtp.start_page("domingo")
        sense = Sense()
        self.wxr.wtp.add_page(
            "Plantilla:ámbito",
            10,
            ":*'''Ámbito:''' México[[Categoría:ES:México|DOMINGO]]",
        )
        root = self.wxr.wtp.parse("{{ámbito|México}}")
        process_ambito_template(self.wxr, sense, root.children[0])
        self.assertEqual(
            sense.model_dump(exclude_defaults=True),
            {"categories": ["ES:México"], "tags": ["Mexico"]},
        )
