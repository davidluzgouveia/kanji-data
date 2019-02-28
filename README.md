# Kanji Data

This repository contains a [JSON file](kanji.json) combining all of the kanji data that I found relevant to my studies of the Japanese language. There are also two smaller variants containing only the [kyouiku](kanji-kyouiku.json) and [jouyou](kanji-jouyou.json) subsets.

Most of the data is the same as the KANJIDIC dataset, but converted to JSON for ease of use, stripped of information I didn't need, and improved with updated JLPT levels and WaniKani content.

The Python scripts used to extract and organize all of the data are also provided. Even if my choice of fields does not match your requirements, the scripts might still be useful to extract what you need.

## References

All of the data comes from the following sources:

- Kanji: [KANJIDIC](http://www.edrdg.org/wiki/index.php/KANJIDIC_Project)
- JLPT: [Jonathan Waller's JLPT Resources page](http://www.tanos.co.uk/jlpt/)
- WaniKani: [WaniKani API](https://docs.api.wanikani.com/)