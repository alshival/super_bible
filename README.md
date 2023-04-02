# super_bible
A database of verses from the Holy Bible and the Gospel of Mary Magdalene. The `super_bible` database can be downloaded as a CSV file (`SUPER_BIBLE/super_bible.csv`), a pickle file (`SUPER_BIBLE/super_bible.pkl`) for importing into python's pandas, and a SQLite3 database (`SUPER_BIBLE/super_bible.db`). 

Individual translations, such as for the English Standard Version (`SUPER_BIBLE/super_bible_ESV.pkl`), are also available.
## Data Fields Chart
|**testament**|**book**|**title**|**chapter**|**verse**|**text**|**version**|**language**|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|string|int64|string|int64|int64|string|string|string|
|OT for old testament. NT for new testament.|Book ID of the book containing the verse.|Title of the book containing the verse.|Chapter containing the verse.|The verse number.|The verse|The translation abbreviation (e.g. KSGM for [King Samuel's Gospel of Mary Magdalene](www.gospelmarymagdalene.com)).|Currently supported langages are English (EN) and Spanish (ES).|

## Sample Data
|testament|book|title|chapter|verse|text|version|language|
|:-:|:-:|:--:|:-:|:-:|:-------:|:-:|:-:|
|OT|	1|	Genesis|	1|	1|	In the beginning, God created the heavens and ...|	ESV|	EN|
|OT|	1|	Genesis|	1|	2|	The earth was without form and void, and darkn...|	ESV|	EN|
|OT|	1|	Genesis|	1|	3|	And God said, "Let there be light," and there ...|	ESV|	EN|
|OT|	1|	Genesis|	1|	4|	And God saw that the light was good. And God s...|	ESV|	EN|
|OT|	1|	Genesis|	1|	5|	God called the light Day, and the darkness he ...|	ESV|	EN|
|...|	...|	...|	...|	...|	...|	...|	...|
|NT|	777|	Evangelio de Maria Magdalena|	4|	119|	como él nos mandó.	|RSEM|	ES|
|NT|	777|	Evangelio de Maria Magdalena|	4|	120|	Debemos predicar el evangelio y no establecer ...	|RSEM|	ES|
|NT|	777|	Evangelio de Maria Magdalena|	4|	122|	Después que Levi termino de hablar, se fueron ...	|RSEM|	ES|
|NT|	777|	Evangelio de Maria Magdalena|	4|	123|	Rey Samuel's El Evangelio de Maria	|RSEM|	ES|



The goal is to include as many translations as possible in as many languages as possible, though at the moment, the database only includes the following:

   <ul>
     <li>English
       <ul>
         <li>AMP (The Amplified Bible)</li>
         <li>ESV (English Standard Version)</li>
         <li>KJV (King James Version)</li>
         <li>NASB (New American Standard Bible)</li>
         <li>NKJV (New King James Version)</li>
         <li>KSGM (King Samuel's Gospel of Mary)</li>
       </ul>
     </li>
     <li> Spanish
       <ul>
         <li>RV1909 (Reina Valera 1909)</li>
         <li>RV1858 (Reina Valera 1858 NT)</li>
         <li>RVG (Reina Valera Gómez 2010)</li>
         <li>RSEM (Rey Samuel's Evangelio de Maria)</li>
       </ul>
     </li>
   </ul>

This data was put together with the intention of creating a dataset of the scripture to train large language models, such as Chat GPT-4, and is presented in this repository in its rawest form.

The raw files used to construct the `super_bible` dataset can be found in the `zraw_dir/`. Getting the scripture in this raw format does take some time, but worth the effort. Some of these I found online; others I constructed myself. The script is written in such a way that makes it easy to incorporate additional languages. The python script `bible_data_prep.ipynb` generates the `super_bible` dataset from raw CSV/TSV files contained in the `zraw_dir/` directory.

The SQLite3 database contains the `super_bible` in a table titled as such, along with a few useful SQL views:

    create view ESV as
      select * from super_bible
      where version = 'ESV'

So instead of typing 
    
    select * from super_bible
        where version = 'ESV'

you can just use 
    
    select * from esv
    
