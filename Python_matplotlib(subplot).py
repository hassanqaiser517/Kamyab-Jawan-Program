#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[42]:


get_ipython().run_line_magic('matplotlib', 'inline')
a = np.array([2,4,7,6])
b = np.array([9,5,3,6])

plt.subplot(1,1,1)
plt.plot(a, marker = '.', ms=12,mec='k',mfc='b',color = 'b',label = "plot 1")

plt.plot(b)

plt.show()   


# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')
a = np.array([2,4,7,6])
b = np.array([9,4,8,3])

plt.subplot(1,2,1)
plt.plot(a, marker = '.', ms=12,mec='k',mfc='b',color = 'b',linewidth= '1',label = "plot 1")

plt.subplot(1,2,2)
plt.plot(b,marker='.',ms=12,mec = 'k', mfc= 'r',color='r',label = "plot 2")

plt.show()


# In[43]:


get_ipython().run_line_magic('matplotlib', 'inline')
a = np.array([2,4,7,6])
b = np.array([9,6,8,3])
c = np.array([1,3,2,8])

plt.subplot(1,3,1)
plt.plot(a, marker = '.', ms = 12, mec = 'k', mfc = 'b', color = 'b', label = "plot 1")

plt.subplot(1,3,2)
plt.plot(b, marker = '.', ms = 12, mec = 'k', mfc = 'r', color = 'r', label = "plot 2")
 
plt.subplot(1,3,3)
plt.plot(c, marker = '.', ms = 12, mec = 'k', mfc = 'g', color = 'g', label = "plot 3")

plt.show()


# In[47]:


get_ipython().run_line_magic('matplotlib', 'inline')

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
c = np.array([3,4,5,6])
d = np.array([4,5,6,7])

plt.subplot(1,4,1)
plt.plot(a, marker = '.', ms = 12, mec = 'k', mfc = 'b', color = 'b', label = "plot 1")

plt.subplot(1,4,2)
plt.plot(b, marker = '.', ms = 12, mec = 'k', mfc = 'r', color = 'r', label = "plot 2")
 
plt.subplot(1,4,3)
plt.plot(c, marker = '.', ms = 12, mec = 'k', mfc = 'g', color = 'g', label = "plot 3")

plt.subplot(1,4,4)
plt.plot(d, marker = '.', ms = 12, mec = 'k', mfc = 'b', color = 'b', label = "plot 4")

plt.show()


# In[48]:


get_ipython().run_line_magic('matplotlib', 'inline')

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
c = np.array([3,4,5,6])
d = np.array([4,5,6,7])
e = np.array([5,6,7,8])

plt.subplot(1,5,1)
plt.plot(a, marker = '.', ms = 12, mec = 'k', mfc = 'b', color = 'b', label = "plot 1")

plt.subplot(1,5,2)
plt.plot(b, marker = '.', ms = 12, mec = 'k', mfc = 'r', color = 'r', label = "plot 2")
 
plt.subplot(1,5,3)
plt.plot(c, marker = '.', ms = 12, mec = 'k', mfc = 'g', color = 'g', label = "plot 3")

plt.subplot(1,5,4)
plt.plot(d, marker = '.', ms = 12, mec = 'k', mfc = 'b', color = 'b', label = "plot 4")

plt.subplot(1,5,5)
plt.plot(e, marker = '.', ms = 12, mec = 'k', mfc = 'r', color = 'r', label = "plot 5")

plt.show()


# In[52]:


get_ipython().run_line_magic('matplotlib', 'inline')

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
c = np.array([3,4,5,6])
d = np.array([4,5,6,7])
e = np.array([5,6,7,8])
f = np.array([6,7,8,9])

plt.subplot(1,6,1)
plt.plot(a, marker = '.', ms = 12, mec = 'k', mfc = 'b', color = 'b', label = "plot 1")

plt.subplot(1,6,2)
plt.plot(b, marker = '.', ms = 12, mec = 'k', mfc = 'r', color = 'r', label = "plot 2")
 
plt.subplot(1,6,3)
plt.plot(c, marker = '.', ms = 12, mec = 'k', mfc = 'g', color = 'g', label = "plot 3")

plt.subplot(1,6,4)
plt.plot(d, marker = '.', ms = 12, mec = 'k', mfc = 'b', color = 'b', label = "plot 4")

plt.subplot(1,6,5)
plt.plot(e, marker = '.', ms = 12, mec = 'k', mfc = 'r', color = 'r', label = "plot 5")

plt.subplot(1,6,6)
plt.plot(f, marker = '.', ms = 12, mec = 'k', mfc = 'g', color = 'g', label = "plot 6")

plt.show()


# In[ ]:




