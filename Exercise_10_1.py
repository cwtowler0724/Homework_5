#!/usr/bin/env python
# coding: utf-8

# In[2]:


def nested_sum(t):
    count = 0
    for nestedList in t:
        count += sum(nestedList)
    return count


# In[3]:


t = [[1, 2], [3], [4, 5, 6]]


# In[4]:


print(nested_sum(t))


# In[ ]:




