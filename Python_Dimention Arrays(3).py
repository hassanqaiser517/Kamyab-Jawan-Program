#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
g = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

q = g.reshape(4,2)
print(g)


# In[20]:


for x in g:
    for y in x:
        print(y)


# In[21]:


q =  np.array([range(100)])
print(g)

for id1, x in np.ndenumerate(g):
    print(id1,x)


# In[26]:


#Using Concatenate
g = np.array([[1,2],[3,4]])
h = np.array([[5,6],[7,8]])

i = np.concatenate((g,h))
print(i)


# In[37]:


g = np.array([[1,2],[3,4]])
h = np.array([[5,6],[7,8]])

#Giving axix
i = np.concatenate((g,h), axis=1)
print(i)


# In[38]:


#Using stack
g = np.array([[1,2],[3,4]])
h = np.array([[5,6],[7,8]])

i = np.stack((g,h))
print(i)


# In[31]:


g = np.array([[1,2],[3,4]])
h = np.array([[5,6],[7,8]])

#using Horizontal stack
i = np.hstack((g,h))
print(i)


# In[39]:


g = np.array([[1,2],[3,4]])
h = np.array([[5,6],[7,8]])

#using Vertical stack
i = np.vstack((g,h))
print(i)


# In[40]:


g = np.array([range(9)])
print(g)


# In[ ]:




