import json

# Takes kanjidic.json and combines it with jlpt.json and wanikani.json

with open("jlpt.json", "rt", encoding="utf-8") as fp:
    jlpt = json.load(fp)

with open("wanikani.json", "rt", encoding="utf-8") as fp:
    wanikani = json.load(fp)

with open("kanjidic.json", "rt", encoding="utf-8") as fp:
    kanjidic = json.load(fp)

output = {}

# Start with all the entries that are actually in WaniKani to preserve order
for key, wanikani_value in wanikani.items():
    if key not in kanjidic: # catches the "repeater" kanji that WaniKani has
        continue
    kanjidic_value = kanjidic[key]
    entry = {
        "strokes": kanjidic_value["strokes"],
        "grade": kanjidic_value["grade"],
        "freq": kanjidic_value["freq"],
        "jlpt_old": kanjidic_value["jlpt"],
        "jlpt_new": jlpt[key] if key in jlpt else None,
        "meanings": kanjidic_value["meanings"],
        "readings_on": kanjidic_value["readings_on"],
        "readings_kun": kanjidic_value["readings_kun"],
        "wk_level": wanikani_value["level"],
        "wk_meanings": wanikani_value["meanings"],
        "wk_readings_on": wanikani_value["readings_on"],
        "wk_readings_kun": wanikani_value["readings_kun"],
        "wk_radicals": wanikani_value["radicals"],
    }
    output[key] = entry

# Then add the remaining entries that do not exist in WaniKani
for key, kanjidic_value in kanjidic.items():
    if key in output:
        continue
    entry = {
        "strokes": kanjidic_value["strokes"],
        "grade": kanjidic_value["grade"],
        "freq": kanjidic_value["freq"],
        "jlpt_old":  kanjidic_value["jlpt"],
        "jlpt_new": jlpt[key] if key in jlpt else None,
        "meanings": kanjidic_value["meanings"],
        "readings_on": kanjidic_value["readings_on"],
        "readings_kun": kanjidic_value["readings_kun"],
        "wk_level": None,
        "wk_meanings": None,
        "wk_readings_on": None,
        "wk_readings_kun": None,
        "wk_radicals": None,
    }
    output[key] = entry

with open("..\\kanji.json", "wt", encoding="utf-8") as fp:
    json.dump(output, fp, indent=4, ensure_ascii=False)