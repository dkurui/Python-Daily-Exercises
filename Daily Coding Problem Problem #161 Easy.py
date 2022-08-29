#!/usr/bin/env python
# coding: utf-8

# In[17]:


def inverse(bin_str):
    fin_str = []
    for i in bin_str:
        if i == '1':
            fin_str.append('0')
        elif i == '0':
            fin_str.append('1')
        else:
            fin_str.append(" ")
    fin_str = ''.join(fin_str)
    return fin_str


# In[18]:


sample_str = '1111 0000 1111 0000 1111 0000 1111 0000'


# In[19]:


inverse(sample_str)


# In[ ]:




