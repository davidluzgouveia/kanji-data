import json

# Processes the files created by wanikani-get into a simpler format
# Outputs wanikani.json with a list of all kanjis in WaniKani and associated information
# Each kanji has information on its level, radicals, meanings and readings
# Note: Meanings and readings get a prefix ^ if not primary and ! if not accepted

radicals = {}
kanjis = {}

def process_radicals():
    with open("wanikani-radical.json", "rt", encoding="utf-8") as fp:
        input = json.load(fp)
    for entry in input:
        id = entry["id"]
        data = entry["data"]
        meaning = data["meanings"][0]["meaning"]
        radicals[id] = meaning

def get_prefix(value):
    if not value["accepted_answer"]:
        return "!"
    if not value["primary"]:
        return "^"
    return ""

def process_kanjis():
    with open("wanikani-kanji.json", "rt", encoding="utf-8") as fp:
        input = json.load(fp)
    for entry in input:
        data = entry["data"]
        kanji = {
            "level": 0,
            "meanings": [],
            "readings_on": [],
            "readings_kun": [],
            "radicals": [],
        }
        characters = data["characters"]
        kanjis[characters] = kanji
        kanji["level"] = data["level"]
        for meaning in data["meanings"]:
            kanji["meanings"].append(get_prefix(meaning) + meaning["meaning"])
        for reading in data["readings"]:
            value = reading["reading"]
            if value == "None":
                continue
            if reading["type"] == "onyomi":
                kanji["readings_on"].append(get_prefix(reading) + value)
            elif reading["type"] == "kunyomi":
                kanji["readings_kun"].append(get_prefix(reading) + value)
        for radical_id in data["component_subject_ids"]:
            kanji["radicals"].append(radicals[radical_id])

process_radicals()
process_kanjis()

with open("wanikani.json", "wt", encoding="utf-8") as fp:
    json.dump(kanjis, fp, indent=4, ensure_ascii=False)