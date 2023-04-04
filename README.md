# super_bible
A database of verses from the Holy Bible and the Gospel of Mary Magdalene. 

<p align="center">
   <img src="https://github.com/alshival/super_bible/blob/main/zraw_metadata/canvas%20-%202023-01-25T022442.478.png?raw=true"  width="55%" height="55%">
   <img src="https://github.com/alshival/super_bible/blob/main/zraw_metadata/canvas%20(26).png?raw=true"  width="38.5%" height="38.5%">
</p>

The goal is to include as many translations as possible in as many languages as possible, though at the moment, only Engish and Spanish are supported. The `super_bible` database can be downloaded as

   * a CSV file ([`SUPER_BIBLE/super_bible.csv`](https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/super_bible.csv)),
   * a pickle file ([`SUPER_BIBLE/super_bible.pkl`](https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/super_bible.pkl)) for importing into python's pandas, or 
   * a SQLite3 database ([`SUPER_BIBLE/super_bible.db`](https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/super_bible.db)). 

Individual translations, such as for the English Standard Version ([`SUPER_BIBLE/version_files/super_bible_ESV.csv`](https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_ESV.csv)), are also available.


## super_bible - Languages/Translations
The `super_bible` is working towards incorporating more languages and translations. Currently, it includes the following languages/translations:

   <ul>
     <li>English (EN)
       <ul>
         <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_AMP.csv",target="_blank">AMP</a> (The Amplified Bible)</li>
         <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_ASV.csv",target="_blank">ASV</a> (American Standard Version)</li>
         <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_ESV.csv", target="_blank">ESV</a> (English Standard Version)</li>
          <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_KJV.csv", target="_blank">KJV</a> (King James's Version)</li>
          <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_KSGM.csv, target="_blank"">KSGM</a> (King Samuel's Gospel of Mary)</li>
          <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_KSV.csv", target="_blank">KSV</a> (King Samuel's Version)</li>
          <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_NASB.csv", target="_blank">NASB</a> (New American Standard Bible)</li>
          <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_NIV.csv", target="_blank">NIV</a> (New International Version)</li>
          <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_NKJV.csv", target="_blank">NKJV</a> (New King James Version)</li>
          <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_WEB.csv", target="_blank">WEB</a> (World English Bible)</li>
          <li> <a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_YLT.csv", target = "_blank">YLT</a> (Young's Literal Translation)</li>
       </ul>
     </li>
     <li> Español (ES)
       <ul>
          <li><a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_RSEM.csv", target="_blank">RSEM</a> (Rey Samuel's Evangelio de Maria)</li>
          <li><a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_RSV.csv", target="_blank">RSV</a> (Rey Samuel's Versión de La Santa Biblia)</li>
          <li><a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_RV1858.csv", target="_blank">RV1858</a> (Reina Valera 1858 NT)</li>
          <li><a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_RV1909.csv", target="_blank">RV1909</a> (Reina Valera 1909)</li>
         <li><a href="https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/version_files/super_bible_RVG.csv", target="_blank">RVG</a> (Reina Valera Gómez 2010)</li>
       </ul>
     </li>
   </ul>
   
   
## Data Fields Chart
|**testament**|**book**|**title**|**chapter**|**verse**|**text**|**version**|**language**|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|string|int64|string|int64|int64|string|string|string|
|OT/NT for Old/New Testament|Book ID of the book containing the verse|Title of the book containing the verse|Chapter containing the verse|The verse number|The verse|The translation abbreviation|Language abbreviation|

## Sample Data
|testament|book|title|chapter|verse|text|version|language|
|:-:|:-:|:--:|:-:|:-:|:-------:|:-:|:-:|
|OT|	1|	Genesis|	1|	1|	In the beginning, God created the heavens and ...|	ESV|	EN|
|OT|	1|	Genesis|	1|	2|	The earth was without form and void, and darkn...|	ESV|	EN|
|...|	...|	...|	...|	...|	...|	...|	...|
|NT|	777|	Evangelio de Maria Magdalena|	4|	122|	Después que Levi termino de hablar, se fueron ...	|RSEM|	ES|
|NT|	777|	Evangelio de Maria Magdalena|	4|	123|	Rey Samuel's El Evangelio de Maria	|RSEM|	ES|


This data was put together with the intention of creating a dataset of the scripture to train large language models, such as those in openAI's GPT-4 and Google's Bard, and thus is presented in this repository in its purest form. The code used to generate the `super_bible` was made flexible enough so that additional languages can be incorporated.

My intention is to create Ai that can pull up scripture and even chapters easily. The Ai will also help me pinpoint verses that I vaguely remember but cannot pinpoint in the Holy Bible.

Also, I was interested in using an LLM as a codex. I am curious if we can embed a message in the Ai. Perhaps by including the message in the training data.

I call it the Ai Codex.

# The Ai Codex
The Ai Codex is a codex that uses Ai. Suppose you have a secret message `{secret_message}` that you want to get to someone but are afraid of someone intercepting it.

The idea behind the Ai codex is to embed that message in a large language model (LLM) that generates random text. But the LLM will generate `{secret_message}` if a `{secret_phrase}` is passed to the LLM. The idea is to bias the training data in just the right way, as well as picking a secure `{secret_phrase}`.

If you are familiar with neural networks or even random forests, then LLMs will be an easy concept to understand. It behaves sort of like a random forest classification algorithm, but with text. 

Using training data, you can construct a pretrained model $M$. This model can be thought of as a function, $M:x\mapsto M(x)$. The idea is to bias the training data for $M$ so that $$M(\{secret_phrase\}) = \{secret_message\}$$, and try to make 
$$P(M(\{random_text\}) = \{secret_message\})$$
sufficiently small.


# Adding additional languages
To summarize how to add additional languages one must:
 1. create the index file for the language `zraw_metadata/{language}_book_index.txt`
 2. create the directory `zraw_data/{language}`. This directory will host the raw files used to generate the `super_bible` dataset.
 3. generate the raw files for import.
 4. rename the raw files to the version abbreviation (e.g. `KJV.csv` for King James Version).

### Create the index file
First, you need to generate `zraw_metadata/{language}_book_index.txt`. Any additional languages we wish to add require this index file. As example files, see [`zraw_metadata/ES_book_index.txt`](https://github.com/alshival/super_bible/blob/main/zraw_metadata/ES_book_index.txt) and [`zraw_metadata/EN_book_index.txt`](https://github.com/alshival/super_bible/blob/main/zraw_metadata/EN_book_index.txt). These files contain information about the Bibles that are used during import. 

Here is what an index file would look like, though the only fields used are `book`,`title`, and `testament`. 

    book,osisID,title,total_chapters,testament
    1,Gen,Génesis,50,OT
    2,Exod,Éxodo,40,OT
    3,Lev,Levítico,27,OT
    4,...
    64,3Juan,3 Juan,1,NT
    65,Jud,Judas,1,NT
    66,Rev,Revelación,22,NT
    777,Mar,Evangelio de Maria,4,NT

### Create the language directory
The python script `bible_data_prep.ipynb` generates the `super_bible` dataset from raw CSV/TSV files contained in the `zraw_data/` directory. Within `zraw_data/` are folders labeled with the language abbreviation:

* `zraw_data/EN` - folder containing raw English files.
* `zraw_data/ES` - folder containing raw Spanish files.

### Generate the raw files
Here is an example raw file. Note the lack of a header row `[book,chapter,verse,text]`: 

    1,1,1,En el principio creó Dios el cielo y la tierra.
    1,1,2,"Y la tierra estaba desordenada y vacía, y las tinieblas [estaban] sobre la faz del abismo, y el Espíritu de Dios se movía sobre la faz de las aguas."
    1,1,3,Y dijo Dios: Sea la luz; y fue la luz.
    1,1,4,Y vio Dios que la luz [era] buena y separó Dios la luz de las tinieblas.

Getting the scripture in this raw format does take some time, but worth the effort. It streamlines the construction of the `super_bible` dataset to make incorporating additional languages simple. Some of these raw files I found online; others I constructed myself.

### Rename the raw files
The script picks up the filename and uses it to fill the version field in the `super_bible` dataset. Therefore, it is important that you rename the file with the correct abbreviation. For the English Standard Bible (ESV), the required *path+filename* would be `zraw_data/EN/ESV.csv`. For Rey Samuel's Evangelio de Maria (RSEM), the required *path+filename* would be `zraw_data/ES/RSEM.csv. And so on by induction`.

# [`super_bible.db`](https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/super_bible.db)

The SQLite3 database [`SUPER_BIBLE/super_bible.db`](https://github.com/alshival/super_bible/blob/main/SUPER_BIBLE/super_bible.db) contains the `super_bible` in a table titled as such, along with a few useful SQL views:

    create view ESV as
      select * from super_bible
      where version = 'ESV'

So instead of typing 
    
    select * from super_bible
        where version = 'ESV'

you can just use 
    
    select * from esv
    
You can use the SQLite database with Python as well:
    
    import pandas as pd
    import sqlite3
    
    db = sqlite3.connect('SUPER_BIBLE/super_bible.db')
    
    # Query using pandas (returns dataframe object)
    pd.read_sql('select * from super_bible limit 10', con=db)
    
    # Query using SQLite (returns list object)
    res = db.execute("select * from super_bible limit 10')
    res.fetchall()
    
    # Create a view or table that contains a specific language
    db.execute("""
       CREATE VIEW english AS
         select * from super_bible where language = 'EN'""")
    pd.read_sql('select * from english limit 10',con=db)
    
