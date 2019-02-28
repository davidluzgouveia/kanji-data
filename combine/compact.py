# Compacts the JSON outputs from kanjidic, wanikani and combine

with open("input.json", "rt", encoding="utf-8") as fp:
    input = fp.read()

output = input.replace("\n            ", "")
output = output.replace("\n        ]", "]")    

with open("output.json", "wt", encoding="utf-8") as fp:
    fp.write(output)