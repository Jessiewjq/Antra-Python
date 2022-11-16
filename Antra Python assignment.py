#!/usr/bin/env python
# coding: utf-8

# # 1. Create a script that will read and parse the given files and remove duplicates using python, then write back into a single CSV
# ○ When two rows are duplicates, they have the same information but might have different separators/casing. For example
# ■ “1234567890” instead of “123-456-7890”
# ■ “JANE” instead of “Jane”
# ■ “ Tom” instead of “Tom” ■...
# ○ Once you clean up the anomalies, two rows that are supposed to be duplicates should have the exact same information/format.

# In[15]:


import os
from pathlib import Path

path = Path('/Users/jessiewu/Desktop')
os.chdir(path)


# In[16]:


os.getcwd()


# In[42]:


p1 = pd.read_csv("people_1.txt",delimiter = "\t")


# In[38]:


p1


# In[24]:


p2 = pd.read_csv("people_1.txt",delimiter = "\t")


# In[25]:


p2


# In[48]:


def clean(df):
    df['FirstName'] = df['FirstName'].str.lower()
    df['LastName'] = df['LastName'].str.lower()
    df['Phone']=df['Phone'].replace("-","",regex=True)
    df['Address']=df['Address'].replace('No.','',regex=True).replace('#','',regex=True)
    df = df.apply(lambda x : x.str.strip())
    df=df.drop_duplicates()
    return df


# In[49]:


clean(p1)


# In[50]:


clean(p2)


# In[ ]:





# # 2. Split movie.json into 8 smaller JSON files.

# In[51]:


movie=pd.read_json('movie.json')
movie


# In[53]:


chunks = len(movie)//8
for i in range(0,len(movie), chunks):
    print(movie[i:i+chunks])

