# master_bible
A database of verses from the Holy Bible and the Gospel of Mary Magdalene. The goal is to include as many translations as possible in as many languages as possible, though at the moment, the database only contains entries for versus from AMP,ESV,KJV,KSGM (King Samuel's Gospel of Mary), NASB, and NKJV.

This data was put together with the intention of creating a dataset of the scripture to train large language models, such as Chat GPT-4, and is presented in this repository in its rawest form.

|book|title|chapter|verse|text|version|
|:---:|:---:|:---:|:---:|:------:|:---:|
|int64|string|int64|int64|string|string|

The CSVs (minus KSGM) were obtained [here](http://my-bible-study.appspot.com/), and are stored in the folder `bible_csvs`. There is only one .tsv file in that directory at the moment, which is for King Samuel's Gospel of Mary. Any future translations that we add will be kept there.
