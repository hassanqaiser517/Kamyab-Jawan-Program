#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[2]:


array = numpy.array([1,2,3,4,5])
print(array)


# In[3]:


print(type(array))


# In[20]:


import numpy as np
array = np.array([[[3,5],[4,9]],[[3,6],[4,3]]])
print(array)


# In[21]:


print(np.__version__)


# In[22]:


print(array.ndim)


# In[36]:


array_1=np.array([[[12,23,34,45],[64,81,26,69]],[[43,36,58,61],[28,60,43,72]]])
print(array_1[0,-1,-1])


# In[26]:


array_1[3]=array_1[1] + array_1[2]
print(array_1[3])


# In[42]:


array_1=np.array([1,2,3,4,5,6,7,8,9])
print(array_1[0:9])


# In[43]:


array_1=np.array([1,2,3,4,5,6,7,8,9])
print(array_1[0:9:1])


# In[44]:


array_1=np.array([1,2,3,4,5,6,7,8,9])
print(array_1[0:9:2])


# In[45]:


array_1=np.array([1,2,3,4,5,6,7,8,9])
print(array_1[0:9:3])


# In[ ]:




