# super_bible
A database of verses from the Holy Bible and the Gospel of Mary Magdalene. The goal is to include as many translations as possible in as many languages as possible, though at the moment, the database only includes the following:

    * Efrom AMP, ESV, KJV, KSGM (King Samuel's Gospel of Mary), NASB, NKJV.
<ol>
  <li>English
    <ol>
      <li>AMP</li>
      <li>ESV</li>
      <li>KJV</li>
      <li>KSGM (King Samuel's Gospel of Mary)</li>
      <li>NASB</li>
      <li>NKJV</li>
    </ol>
  </li>
  <li> Spanish
    <ol>
        <li>RSEM (Rey Samuel's Evangelio de Maria)</li>
    </ol>
  </li>
</ol>

This data was put together with the intention of creating a dataset of the scripture to train large language models, such as Chat GPT-4, and is presented in this repository in its rawest form.

|testament|book|title|chapter|verse|text|version|
|:---:|:---:|:---:|:---:|:---:|:------:|:---:|
|string|int64|string|int64|int64|string|string|



The `super_bible` dataset is contained in the folder `SUPER_BIBLE`.You will also find .csv files for each individual translation in the `super_bible` format. You will also find a `super_bible.pkl` file which can be imported easily into python using Pandas.  I like pickle files because I sometimes use them to share pre-trained machine-learning models. There is also a CSV file and a SQLite3 database. The SQLite3 database contains the `super_bible` in a table titled as such, along with a few useful SQL views:

    create view ESV as
      select * from super_bible
      where version = 'ESV'

So instead of typing 
    
    select * from super_bible
        where version = 'ESV'

you can just use 
    
    select * from esv

The CSVs (minus KSGM) were obtained [here](http://my-bible-study.appspot.com/), and are stored in the folder `zraw_dir`.
