#!/usr/bin/env python
# coding: utf-8

# In[1]:


def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True  


# In[2]:


fin = open('words.txt')


# In[3]:


count = 0


# In[4]:


num_of_words = 0


# In[5]:


for line in fin:
    num_of_words = num_of_words + 1
    word = line.strip()
    if has_no_e(word) == True:
        count += 1
        print(word)


# In[29]:


percent = (round(count/num_of_words * 100))


# In[30]:


print ('Percentage of words without an e:  ', percent, '%')


# In[ ]:




