import json

# Generates two subsets of the input.json file, one for kyouiku and one for jouyou

with open("kanji.json", "rt", encoding="utf-8") as fp:
    input = json.load(fp)

kyouiku = {}
jouyou = {}

for key, value in input.items():
    grade = value["grade"]
    if grade is None or grade == 9 or grade == 10:
        continue
    if grade != 8:
        kyouiku[key] = value
    jouyou[key] = value

with open("kanji-kyouiku.json", "wt", encoding="utf-8") as fp:
    json.dump(kyouiku, fp, indent=4, ensure_ascii=False)

with open("kanji-jouyou.json", "wt", encoding="utf-8") as fp:
    json.dump(jouyou, fp, indent=4, ensure_ascii=False)