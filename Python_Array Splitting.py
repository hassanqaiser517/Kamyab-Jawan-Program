#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

f = np.array([[2,3,4],
              [5,5,6]])

g = np.array([1,2,3,4,5,6,7,8,9,10])
print(g)

h = np.array_split(g, 5)
print(h)


# In[2]:


g = np.array([[1,2,3],[4,5,6],[7,8,9]])
h = np.array_split(g,3)
print(h)


# In[ ]:





# In[ ]:




