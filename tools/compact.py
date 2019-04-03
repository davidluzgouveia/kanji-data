# Compacts the JSON outputs from kanjidic, wanikani and combine
# Special input values: kanji, wanikani, kanjidic

def compact(input_filename, output_filename):
    with open(input_filename, "rt", encoding="utf-8") as fp:
        input_data = fp.read()
    output_data = input_data.replace("\n            ", "")
    output_data = output_data.replace("\n        ]", "]")
    with open(output_filename, "wt", encoding="utf-8") as fp:
        fp.write(output_data)

input_filename = input("Enter input filename: ")

if input_filename == "kanji":
    compact("..\\kanji.json", "..\\kanji.json")
    compact("..\\kanji-jouyou.json", "..\\kanji-jouyou.json")
    compact("..\\kanji-kyouiku.json", "..\\kanji-kyouiku.json")
    compact("..\\kanji-wanikani.json", "..\\kanji-wanikani.json")
elif input_filename == "wanikani":
    compact("wanikani.json", "wanikani.json")
elif input_filename == "kanjidic":
    compact("kanjidic.json", "kanjidic.json")
else:
    output_filename = input("Enter output filename: ")
    compact(input_filename, output_filename)