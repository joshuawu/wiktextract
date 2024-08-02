from unittest import TestCase

from wikitextprocessor import Wtp
from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.ja.models import Sound, WordEntry
from wiktextract.extractor.ja.sound import extract_sound_section
from wiktextract.wxr_context import WiktextractContext


class TestJaSound(TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.wxr = WiktextractContext(
            Wtp(lang_code="ja"),
            WiktionaryConfig(
                dump_file_lang_code="ja",
                capture_language_codes=None,
            ),
        )

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()

    def test_en_sounds(self):
        self.wxr.wtp.start_page("puppy")
        self.wxr.wtp.add_page(
            "テンプレート:IPA",
            10,
            '[[w:国際音声記号|IPA]]: <span class="IPA">/ˈpə.pi/</span>, <span class="IPA">/ˈpʌp.i/</span>[[カテゴリ: 国際音声記号あり]]',
        )
        self.wxr.wtp.add_page(
            "テンプレート:X-SAMPA",
            10,
            '[[w:X-SAMPA|X-SAMPA]]:&nbsp;<span title="X-SAMPA pronunciation">/<span class="SAMPA">"p@.pi</span>/, /<span class="SAMPA">"pVp.i</span>/</span>',
        )
        self.wxr.wtp.add_page(
            "テンプレート:X-SAMPA",
            10,
            '<table class="audiotable"><tr><td class="unicode audiolink" style="padding-right:5px; padding-left: 0;">音声 (米)<td class="audiofile">[[File:en-us-puppy.ogg|noicon|175px]]</td><td class="audiometa" style="font-size: 80%;">([[:File:en-us-puppy.ogg|ファイル]])</td></tr></table>[[カテゴリ:英語 音声リンクがある語句|PUPPY]]',
        )
        data = WordEntry(lang="英語", lang_code="en", word="puppy")
        root = self.wxr.wtp.parse("""* {{IPA|ˈpə.pi|ˈpʌp.i}}
* {{X-SAMPA|"p@.pi|"pVp.i}}
* {{音声|en|en-us-puppy.ogg|音声 (米)}}""")
        extract_sound_section(self.wxr, data, root)
        self.assertEqual(
            data.categories, ["国際音声記号あり", "英語 音声リンクがある語句"]
        )
        self.assertEqual(
            data.sounds[:4],
            [
                Sound(ipa="ˈpə.pi"),
                Sound(ipa="ˈpʌp.i"),
                Sound(ipa='"p@.pi', tags=["X-SAMPA"]),
                Sound(ipa='"pVp.i', tags=["X-SAMPA"]),
            ],
        )
        self.assertEqual(data.sounds[4].audio, "en-us-puppy.ogg")
        self.assertEqual(data.sounds[4].raw_tags, ["音声 (米)"])
