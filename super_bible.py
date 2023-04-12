#!/usr/bin/env python
# coding: utf-8

# # `super_bible` Data Prep

# This notebook is used to create the `super_bible` dataset. Data is first put together as a pandas dataframe, then converted into various formats.
# 
# You need the following python packages:

# In[1]:


import os
import pandas as pd
import regex as re
import csv
import sqlite3


# If your working directory is the top-level directory of the github repository, then this code will fetch the filenames for the csvs stored in the `zraw_data` folder

# In[2]:


zraw_dir = ".zraw_data/"
languages = os.listdir(zraw_dir)
languages


# The `book_index.txt` file contains more information about the chapters than what is provided in the CSV files we downloaded. This function imports the correct index file depending on the language.

# In[3]:


def bible_index(language):
    return pd.read_csv(f'.zraw_metadata/{language}_book_index.txt',names=['book','osisID','title','total_chapters','testament'],skiprows=1)


# In[4]:


bible_index('EN')


# This is the backbone of the import. It will import the .csv/.tsv files and prep the data.

# In[5]:


def import_bible(filename,language='EN'):
    if not (re.search('\\.tsv',filename)==None):
        dat = pd.read_csv(f'{zraw_dir}{language}/{filename}',
                          sep='\t',
                          names=['book','chapter','verse','text'],
                          header=None)
        dat['version'] = re.sub('\\.tsv','', filename)
    else:
        dat = pd.read_csv(f'{zraw_dir}{language}/{filename}',
                          lineterminator='\n',
                          header=None, 
                          names=['book','chapter','verse','text'], 
                          escapechar='\\')
        dat['version'] = re.sub('\\.csv','', filename)
    
    dat = bible_index(language)[['testament','book','title']].merge(dat,on=['book'])
    dat['language']=language
    dat = dat
    
    return dat 


# Here, we generate the `super_bible` dataset. We import by language so that we know which title to use.

# In[6]:


sb = []
for language in languages:
    csvs = pd.Series([(file,language) for file in os.listdir(zraw_dir + language)])
    sb = sb + [import_bible(*csv) for csv in csvs]

super_bible = pd.concat(sb,axis = 0).astype({'testament':'string','title':'string','text':'string','version':'string','language':'string'}).drop_duplicates()


# In[7]:


super_bible


# In[8]:


super_bible.dtypes


# Now we save as various formats.

# ## Export `super_bible` 

# In[9]:


output_dir = 'SUPER_BIBLE/'


# In[10]:


super_bible.drop_duplicates().to_pickle(output_dir + 'super_bible.pkl')


# In[11]:


super_bible.drop_duplicates().to_csv(output_dir + 'super_bible.csv',index=False,quoting=csv.QUOTE_NONNUMERIC)


# ### super_bible SQLite3

# In[12]:


conn = sqlite3.connect(output_dir + 'super_bible.db')

super_bible.to_sql('super_bible',con=conn,index=False,if_exists='replace')

bible_csvs=[]
for language in languages:
    bible_csvs = bible_csvs + os.listdir(zraw_dir + language)

tbls = pd.Series(bible_csvs).apply(lambda x: re.sub('\\..*','',x)).tolist()
for i in tbls:
    conn.execute(f"""
    DROP VIEW IF EXISTS {i} 
    """)
    conn.execute(f"""
    CREATE VIEW {i} AS
    select * from super_bible
    where version = '{i}'
    """)
    
conn.close()


# # Individual Translations

# In[13]:


for i in bible_csvs:
    version = re.sub('\\..*','',i)
    super_bible[super_bible['version']==version].drop_duplicates().to_csv(f'SUPER_BIBLE/version_files/super_bible_{version}.csv',index=False,quoting=csv.QUOTE_NONNUMERIC)
    super_bible[super_bible['version']==version].drop_duplicates().to_pickle(f'SUPER_BIBLE/version_files/super_bible_{version}.pkl')

