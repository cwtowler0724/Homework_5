#!/usr/bin/env python
# coding: utf-8

# In[1]:


fin = open('words.txt')


# In[2]:


for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)


# In[ ]:




