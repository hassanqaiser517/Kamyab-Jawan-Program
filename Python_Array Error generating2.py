#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy
import numpy as np
a = np.array(["Hassan","Bilal","Fahad"])
print(a.dtype)


# In[6]:


b = np.array(["25","35","45","55"])
print(b.dtype)


# In[7]:


c = np.array([3,4,5,6,7], dtype="i")
print(c.dtype)


# In[8]:


d = np.array([3.1,4.2,5.3,6.4,7.5], dtype="i")
print(d.dtype)


# In[9]:


d = np.array([3.1,4.2,5.3,6.4,7.5], dtype="i")
print(d)


# In[10]:


d = np.array([0,3.1,4.2,5.3,6.4,7.5,], dtype="f")
print(d.dtype)


# In[11]:


e = d.copy()
e[0] = 34
print(d)
print(e)


# In[ ]:




