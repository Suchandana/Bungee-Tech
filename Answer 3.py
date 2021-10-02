#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('C:/Users/sucha/Downloads/internship-test2-master/internship-test2-master/input/question-3/main.csv')


# In[3]:


df_grouped = df.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])


# In[4]:


df_output = df_grouped[['Team', 'Yellow Cards', 'Red Cards']].copy()


# In[5]:


df_output.head()


# In[ ]:




