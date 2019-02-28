import requests
import json
import time

# Queries the WaniKani API (https://docs.api.wanikani.com/) to get all of the subjects data into JSON files on disk
# Outputs three files: wanikani-radical-raw.json, wanikani-kanji-raw.json and wanikani-vocabulary-raw.json
# The format of these files is the same as the one described in the API, but without pagination, and split by type

# IMPORTANT: Put your WaniKani API key here
key = "########-####-####-####-############"
headers = {"Authorization": f"Bearer {key}"}

pages = []
combined = []
radical = []
kanji = []
vocabulary = []

def get_subjects():
    url = "https://api.wanikani.com/v2/subjects"
    get_subjects_page(url, 1)
    combine_pages()

def get_subjects_page(url, count):
    response = requests.get(url, headers=headers)
    page = response.json()
    pages.append(page)
    print(f"Fetched page {count}")
    next_url = page["pages"]["next_url"]
    if next_url != None:
        get_subjects_page(next_url, count+1)
        time.sleep(2)

def combine_pages():
    for page in pages:
        for entry in page["data"]:
            combined.append(entry)

def split_subjects():
    for entry in combined:
        if entry["object"] == "radical":
            radical.append(entry)
        if entry["object"] == "kanji":
            kanji.append(entry)
        if entry["object"] == "vocabulary":
            vocabulary.append(entry)

get_subjects()
split_subjects()

with open("wanikani-radical-raw.json", "wt", encoding="utf-8") as fp:
    json.dump(radical, fp, indent=4, ensure_ascii=False)

with open("wanikani-kanji-raw.json", "wt", encoding="utf-8") as fp:
    json.dump(kanji, fp, indent=4, ensure_ascii=False)

with open("wanikani-vocabulary-raw.json", "wt", encoding="utf-8") as fp:
    json.dump(vocabulary, fp, indent=4, ensure_ascii=False)