# super_bible
A database of verses from the Holy Bible and the Gospel of Mary Magdalene. The goal is to include as many translations as possible in as many languages as possible, though at the moment, the database only contains entries for versus from AMP, ESV, KJV, KSGM (King Samuel's Gospel of Mary), NASB, and NKJV.

This data was put together with the intention of creating a dataset of the scripture to train large language models, such as Chat GPT-4, and is presented in this repository in its rawest form.

|testament|book|title|chapter|verse|text|version|
|:---:|:---:|:---:|:---:|:---:|:------:|:---:|
|string|int64|string|int64|int64|string|string|

The `super_bible` dataset is contained in the folder `SUPER_BIBLE`. In there, you will find a `.pkl` file which can be imported easily into python using Pandas. 

You will also find .csv files for each individual translation in the `super_bible` format.

I like pickle files because I sometimes use them to share pre-trained machine-learning models. There is also a CSV file and a SQLite3 database. The SQLite3 database contains the `super_bible` in a table titled as such, along with a few useful SQL views:

    create view ESV as
      select * from super_bible
      where version = 'ESV'

So instead of typing 
    
    select * from super_bible
        where version = 'ESV'

you can just use 
    
    select * from esv

The CSVs (minus KSGM) were obtained [here](http://my-bible-study.appspot.com/), and are stored in the folder `bible_csvs`. There is only one .tsv file in that directory at the moment, which is for King Samuel's Gospel of Mary. Any future translations that we add will be kept there.
