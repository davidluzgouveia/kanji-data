# Kanji Data

This repository contains a [JSON file](kanji.json) combining all of the kanji data that I found relevant to my studies of the Japanese language. There are also two smaller variants containing only the [kyouiku](kanji-kyouiku.json) and [jouyou](kanji-jouyou.json) subsets.

Most of the data is the same as the KANJIDIC dataset, but converted to JSON for ease of use, stripped of information I didn't need, and extended with updated JLPT levels and WaniKani content.

All of the data was extracted and processed using only scripts, which should decrease the chances of human error - unless there is some bug in the code, in which case it will be easy to fix and regenerate the data.

The Python scripts used to extract and organize all of the data are also provided. Even if my choice of fields does not match your requirements, the scripts might still be useful to extract what you need.

> Note: Some of the meanings and readings that were extracted from WaniKani have a `^` or a `!` prefix. I added these to denote when an item is *not a primary answer* (`^`) or *not an accepted answer* (`!`) on WaniKani. These characters don't appear at the start of any other string in the dataset, so if you prefer to remove them, you can do a simple search and replace from `"^` and `"!` to `"`.

## Example

Here's what a single entry in the file looks like:

```json
"勝": {
    "strokes": 12,
    "grade": 3,
    "freq": 185,
    "jlpt_old": 2,
    "jlpt_new": 3,
    "meanings": ["Victory","Win","Prevail","Excel"],
    "readings_on": ["しょう"],
    "readings_kun": ["か.つ","-が.ち","まさ.る","すぐ.れる","かつ"],
    "wk_level": 9,
    "wk_meanings": ["Win"],
    "wk_readings_on": ["しょう"],
    "wk_readings_kun": ["!か"],
    "wk_radicals": ["Moon","Gladiator","Power"]
}
```

Many of these fields can be `null` so be weary of that. For instance, there are entries that don't exist in WaniKani, or that are not part of the JLPT sets, so those fields will be `null`.

## References

All of the data comes from the following sources:

- Kanji: [KANJIDIC](http://www.edrdg.org/wiki/index.php/KANJIDIC_Project)
- JLPT: [Jonathan Waller's JLPT Resources page](http://www.tanos.co.uk/jlpt/)
- WaniKani: [WaniKani API](https://docs.api.wanikani.com/)
