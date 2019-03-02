import gzip
import json
import requests
import string
import xml.etree.ElementTree as etree

# Converts the KANJIDIC dictionary in xml.gz format into JSON discarding unneeded data
# The data is downloaded by the script from the official KANJIDIC project website
# Outputs kanjidic.json with stroke, grade, freq, jlpt, meanings and readings for every kanji

kanji = {}

def get_kanjidic_data():

    url = "http://www.edrdg.org/kanjidic/kanjidic2.xml.gz"
    request = requests.get(url)
    data = gzip.decompress(request.content)
    xml = data.decode("utf-8")
    tree = etree.fromstring(xml)

    # Source: https://github.com/olsgaard/Japanese_nlp_scripts/blob/master/hiragana_katakana_translitteration.py
    katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
    hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
    kat2hir = str.maketrans(katakana_chart, hiragana_chart)

    for character in tree.iter("character"):
        entry = {
            "strokes": None,
            "grade": None,
            "freq": None,
            "jlpt": None,
            "meanings": [],
            "readings_on": [],
            "readings_kun": []
        }

        literal = character.find("literal").text
        kanji[literal] = entry

        misc = character.find("misc")
        if misc is not None:
            grade = misc.find("grade")
            if grade is not None:
                entry["grade"] = int(grade.text)
            freq = misc.find("freq")
            if freq is not None:
                entry["freq"] = int(freq.text)
            jlpt = misc.find("jlpt")
            if jlpt is not None:
                entry["jlpt"] = int(jlpt.text)
            stroke_count = misc.find("stroke_count")
            if stroke_count is not None:
                entry["strokes"] = int(stroke_count.text)
        
        reading_meaning = character.find("reading_meaning")
        if reading_meaning is not None:
            rmgroups = reading_meaning.findall("rmgroup")
            for rmgroup in rmgroups:
                
                meanings = rmgroup.findall("meaning")
                for meaning in meanings:
                    m_lang = meaning.get("m_lang")
                    if m_lang is None or m_lang == "en":
                        entry["meanings"].append(string.capwords(meaning.text))
                
                readings = rmgroup.findall("reading")
                for reading in readings:
                    r_type = reading.get("r_type")
                    if r_type == "ja_on":
                        entry["readings_on"].append(reading.text.translate(kat2hir))
                    elif r_type == "ja_kun":
                        entry["readings_kun"].append(reading.text)                    

get_kanjidic_data()

with open("kanjidic.json", "wt", encoding="utf-8") as fp:
    json.dump(kanji, fp, ensure_ascii=False, indent=4)