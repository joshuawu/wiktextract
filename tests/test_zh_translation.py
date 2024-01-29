from unittest import TestCase

from wikitextprocessor import Wtp
from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.zh.models import WordEntry
from wiktextract.extractor.zh.translation import extract_translation
from wiktextract.thesaurus import close_thesaurus_db
from wiktextract.wxr_context import WiktextractContext


class TestZhTranslation(TestCase):
    def setUp(self) -> None:
        self.wxr = WiktextractContext(
            Wtp(lang_code="zh"), WiktionaryConfig(dump_file_lang_code="zh")
        )

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()
        close_thesaurus_db(
            self.wxr.thesaurus_db_path, self.wxr.thesaurus_db_conn
        )

    def test_t_template(self):
        self.wxr.wtp.start_page("太陽風")
        self.wxr.wtp.add_page(
            "Template:t+",
            10,
            """{{#switch:{{{3}}}
|f=<span class="gender"><abbr title="陰性名詞">f</abbr></span>
|m=<span class="gender"><abbr title="陽性名詞">m</abbr></span>
}}""",
        )
        self.wxr.wtp.add_page("Template:qualifier", 10, "({{{1}}})")
        page_data = [WordEntry(word="太陽風", lang_code="zh", lang="漢語")]
        wikitext = """{{trans-top|太陽上層大氣射出的超高速電漿流}}
* 希伯来语：{{t+|he|רוח השמש|tr=ruakh ha-shemesh}}、{{t+|he|רוח סולרית|f|tr=ruakh solarit}}
* 塞尔维亚-克罗地亚语：
*: 西里尔字母：{{qualifier|Ekavian}} {{t+|sh|сунчев ветар|m}}"""
        node = self.wxr.wtp.parse(wikitext)
        extract_translation(self.wxr, page_data, node)
        self.assertEqual(
            [
                d.model_dump(exclude_defaults=True)
                for d in page_data[0].translations
            ],
            [
                {
                    "lang_code": "he",
                    "lang": "希伯来语",
                    "sense": "太陽上層大氣射出的超高速電漿流",
                    "word": "רוח השמש",
                    "roman": "ruakh ha-shemesh",
                },
                {
                    "lang_code": "he",
                    "lang": "希伯来语",
                    "sense": "太陽上層大氣射出的超高速電漿流",
                    "word": "רוח סולרית",
                    "roman": "ruakh solarit",
                    "tags": ["陰性名詞"],
                },
                {
                    "lang_code": "sh",
                    "lang": "西里尔字母",
                    "sense": "太陽上層大氣射出的超高速電漿流",
                    "word": "сунчев ветар",
                    "tags": ["Ekavian", "陽性名詞"],
                },
            ],
        )

    def test_link_words(self):
        self.wxr.wtp.start_page("你好")
        page_data = [WordEntry(word="你好", lang_code="zh", lang="漢語")]
        wikitext = """{{翻譯-頂}}
*英语：[[how do you do]]; [[how are you]]"""
        node = self.wxr.wtp.parse(wikitext)
        extract_translation(self.wxr, page_data, node)
        self.assertEqual(
            [
                d.model_dump(exclude_defaults=True)
                for d in page_data[0].translations
            ],
            [
                {
                    "lang_code": "en",
                    "lang": "英语",
                    "word": "how do you do",
                },
                {
                    "lang_code": "en",
                    "lang": "英语",
                    "word": "how are you",
                },
            ],
        )

    def test_subpage_multitrans(self):
        self.wxr.wtp.start_page("英語")
        self.wxr.wtp.add_page(
            "英語/翻譯",
            0,
            """==漢語==
===名詞===
====翻譯====
{{trans-top|一種源於英格蘭的語言}}{{multitrans|data=
* 阿布哈茲語：{{tt|ab|англыз бызшәа}}
* 阿拉貢語：{{t-needed|an}}
}}""",
        )
        page_data = [WordEntry(word="英語", lang_code="zh", lang="漢語")]
        wikitext = "{{trans-see|源於英格蘭的語言|英語/翻譯}}"
        node = self.wxr.wtp.parse(wikitext)
        extract_translation(self.wxr, page_data, node)
        self.assertEqual(
            [
                d.model_dump(exclude_defaults=True)
                for d in page_data[0].translations
            ],
            [
                {
                    "lang_code": "ab",
                    "lang": "阿布哈茲語",
                    "word": "англыз бызшәа",
                    "sense": "一種源於英格蘭的語言",
                }
            ],
        )
