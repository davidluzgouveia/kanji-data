import json

# Takes kanjidic.json and replaces all JLPT values with the ones from jlpt.json
# Also adds in information from wanikani.json, replacing the readings and meanings when possible

with open("..\\jlpt\\jlpt.json", "rt", encoding="utf-8") as fp:
    jlpt = json.load(fp)

with open("..\\wanikani\\wanikani.json", "rt", encoding="utf-8") as fp:
    wanikani_kanji = json.load(fp)    

with open("..\\kanjidic\\kanjidic.json", "rt", encoding="utf-8") as fp:
    kanjidic = json.load(fp)

output = {}

# Start with all the entries that are actually in WaniKani to preserve order
for key, value in wanikani_kanji.items():
    if key not in kanjidic:
        continue
    kanjidic_value = kanjidic[key]
    jlpt_level = jlpt[key] if key in jlpt else None
    entry = {
        "strokes": kanjidic_value["strokes"],
        "grade": kanjidic_value["grade"],
        "freq": kanjidic_value["freq"],
        "jlpt": jlpt_level,
        "wanikani": value["level"],
        "radicals": value["radicals"],
        "meanings": value["meanings"],
        "readings_on": value["readings_on"],
        "readings_kun": value["readings_kun"],
    }
    output[key] = entry

# Then add the remaining ones after
for key, value in kanjidic.items():
    if key in output:
        continue
    jlpt_level = jlpt[key] if key in jlpt else None
    entry = {
        "strokes": value["strokes"],
        "grade": value["grade"],
        "freq": value["freq"],
        "jlpt": jlpt_level,
        "wanikani": None,
        "radicals": None,
        "meanings": value["meanings"],
        "readings_on": value["readings_on"],
        "readings_kun": value["readings_kun"],
    }
    output[key] = entry

with open("..\\kanji.json", "wt", encoding="utf-8") as fp:
    json.dump(output, fp, indent=4, ensure_ascii=False)