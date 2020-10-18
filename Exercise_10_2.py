#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cumsum(t):
    t2 = []
    count = 0
    for i in t:
        count += i
        t2.append(count)
    return t2        


# In[2]:


t = [1, 2, 3]


# In[3]:


print(cumsum(t))


# In[ ]:




