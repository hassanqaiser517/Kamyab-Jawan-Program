#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')

a = np.array([29,31,35,27,25,30,18])
b = np.array([21,34,23,12,15,31,38])

print(np.shape(a))
print(np.shape(b))

plt.scatter(a,b,color='k')
plt.show()


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')

a = np.array([29,31,35,27,25,30,18])
b = np.array([21,34,23,12,15,31,38])
f = np.array([40,41,48,45,33,20])

plt.scatter(a, b, color = 'k')

e = random.randint(10,30,18)

print(e)

c = random.randint(0,100,18)
d = random.randint(0,100,18)

plt.scatter(c,d, color = 'r')

plt.show()


# In[ ]:




