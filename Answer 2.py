#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


df=pd.read_csv('C:/Users/sucha/Downloads/internship-test2-master/internship-test2-master/input/question-2/main.csv')


# In[6]:


df_grouped = df.groupby('occupation')


# In[7]:


df_output = pd.DataFrame(columns=[
        'Occupation',
        'Min',
        'Max'
])


# In[8]:


for item in df_grouped:
    max_age = item[1].max().age
    min_age = item[1].min().age
    new_row = {
        'Occupation': item[0],
        'Min': min_age,
        'Max': max_age
    }
    df_output = df_output.append(new_row, ignore_index=True)


# In[10]:


df_output.head()


# In[ ]:




