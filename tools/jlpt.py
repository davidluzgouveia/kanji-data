import time
import json
import requests
from lxml import html

# Scrapes JLPT kanji and level information from Jonathan Waller's JLPT Resources page (http://www.tanos.co.uk/jlpt/)
# Outputs jlpt.json with a mapping of characters to JLPT levels

jlpt = {}

def get_jlpt_level(level):
    url = f"http://www.tanos.co.uk/jlpt/jlpt{level}/kanji/"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    cells = tree.xpath('//div[@id="contentright"]/table[2]//tr/td[1]/a')
    for cell in cells:
        kanji = cell.text.strip()
        jlpt[kanji] = level

for level in reversed(range(1, 6)):
    get_jlpt_level(level)
    print(f"Fetched data for level {level}")
    time.sleep(2)

with open("jlpt.json", "wt", encoding="utf-8") as fp:
    json.dump(jlpt, fp, indent=4, ensure_ascii=False)