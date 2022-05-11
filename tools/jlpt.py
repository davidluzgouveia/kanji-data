import time
import json
import requests
from lxml import html
import sys

def get_jlpt_level(level):
    url = f"https://jlptsensei.com/jlpt-n{level}-kanji-list/"
    page = requests.get(url)
    content = html.fromstring(page.content)
    table = content.xpath('//*[@id="jl-kanji"]')

    # No use of table header
    # head_tr = table[0].getchildren()[0].findall("tr")[0]
    # for c in head_tr.getchildren():
    #     print(c.text)

    body_tr_list = table[0].getchildren()[1].findall("tr")

    data = list()
    for row in body_tr_list:
        body_td_list = row.findall("td")
        for cell in body_td_list:
            if len(cell.getchildren()) > 0: 
                for c in  cell.getchildren(): 
                    if c.text != ' ':
                        data.append(c.text)
                romaji = cell.getchildren()[0]
                kana = romaji.findall("p")
                if len(kana) > 0: 
                    data.append(kana[0].text)
            else:
                data.append(cell.text)


    kanji_table = []
    nb_columns = 7
    for cell in range(0, len(data), nb_columns):
        kanji_dict = {"kanji":data[cell+1], 
                        "onyomi": 
                            {
                                "romaji":data[cell+2],
                                "kana": data[cell+3], 
                            },
                        "kunyomi": 
                            {
                                "romaji": data[cell+4],
                                "kana": data[cell+5],
                            },
                        "translation":data[cell+6]
                        }
        kanji_table.append(kanji_dict)
    
    return kanji_table




if __name__ == "__main__": 
    if len(sys.argv) < 2:
        print("please give the jlpt level as argument : pyhon jlpt.py 5")
    else :
        level = sys.argv[1]
        if int(level) > 5 or int(level) < 1 : 
            print("wrong level number")
        else: 
            kanji_table = get_jlpt_level(level)
            final_kanji_dict = {f"Jlptn{level}" : kanji_table}
            with open(f"jlptn{level}.json", "wt", encoding="utf-8") as fp:
                json.dump(final_kanji_dict, fp, indent=4, ensure_ascii=False)



