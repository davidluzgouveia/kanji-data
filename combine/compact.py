# Compacts the JSON outputs from kanjidic, wanikani and combine

filename = input("Enter input filename: ")

with open(filename, "rt", encoding="utf-8") as fp:
    input_data = fp.read()

output_data = input_data.replace("\n            ", "")
output_data = output_data.replace("\n        ]", "]")    

filename = input("Enter output filename: ")

with open(filename, "wt", encoding="utf-8") as fp:
    fp.write(output_data)