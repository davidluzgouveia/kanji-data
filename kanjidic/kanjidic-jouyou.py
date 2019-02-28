import json

# Generates two subsets of kanjidic.json, one for kyouiku and one for jouyou

with open("kanjidic.json", "rt", encoding="utf-8") as fp:
    input = json.load(fp)

kyouiku = {}
jouyou = {}

for key, value in input.items():
    grade = value["grade"]
    if grade is None or grade == "9" or grade == "10":
        continue
    if grade != "8":
        kyouiku[key] = value
    jouyou[key] = value

with open("kanjidic-kyouiku.json", "wt", encoding="utf-8") as fp:
    json.dump(kyouiku, fp, indent=4, ensure_ascii=False)

with open("kanjidic-jouyou.json", "wt", encoding="utf-8") as fp:
    json.dump(jouyou, fp, indent=4, ensure_ascii=False)