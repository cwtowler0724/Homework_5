#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import os


# In[3]:


df = pd.read_csv('CSV_2.csv')


# In[4]:


df.head(7)


# In[14]:


ax = df.plot.bar(x = 'event_date', y = 'fatalities')


# In[ ]:




