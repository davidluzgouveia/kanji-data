import time
import json
import requests
from lxml import html

# Scrapes JLPT kanji and level information from Jonathan Waller's JLPT Resources page (http://www.tanos.co.uk/jlpt/)
# Outputs two JSON files, one grouped by level (jlpt-level.json) and another grouped by kanji (jlpt-kanji.json)

output_level = {}
output_kanji = {}

def get_kanji(level):
    url = f"http://www.tanos.co.uk/jlpt/jlpt{level}/kanji/"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    cells = tree.xpath('//div[@id="contentright"]/table[2]//tr/td[1]/a')
    kanjis = []
    for cell in cells:
        kanji = cell.text.strip()
        output_kanji[kanji] = level
        kanjis.append(kanji)
    output_level[level] = kanjis

for level in reversed(range(1, 6)):
    get_kanji(level)
    print(f"Fetched data for level {level}")
    time.sleep(2)

with open("jlpt-level.json", "wt", encoding="utf-8") as fp:
    json.dump(output_level, fp, indent=4, ensure_ascii=False)

with open("jlpt-kanji.json", "wt", encoding="utf-8") as fp:
    json.dump(output_kanji, fp, indent=4, ensure_ascii=False)