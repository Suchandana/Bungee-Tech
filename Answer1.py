#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from pathlib import Path
import numpy as np


# In[10]:


df=pd.read_csv('C:/Users/sucha/Downloads/internship-test2-master/internship-test2-master/input/question-1/main.csv')


# In[4]:


df_grouped = df.groupby((df.Year//10)*10)


# In[11]:


df.head()


# In[12]:


df_output = df[0:0]


# In[13]:


for item in df_grouped:
    population = str(item[1].iloc[[-1]].Population).split()[1]
    new_row_df = item[1].sum()
    new_row = {
        'Year': item[0],
        'Population': population,
        'Total': new_row_df.Total,
        'Violent': new_row_df.Violent,
        'Property': new_row_df.Property,
        'Murder': new_row_df.Murder,
        'Forcible_Rape': new_row_df.Forcible_Rape,
        'Robbery': new_row_df.Robbery,
        'Aggravated_assault': new_row_df.Aggravated_assault,
        'Burglary': new_row_df.Burglary,
        'Larceny_Theft': new_row_df.Larceny_Theft,
        'Vehicle_Theft': new_row_df.Vehicle_Theft
    }
    df_output = df_output.append(new_row, ignore_index=True)


# In[15]:


df_output.head()


# In[ ]:




