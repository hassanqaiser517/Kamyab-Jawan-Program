#!/usr/bin/env python
# coding: utf-8

# In[4]:


x= int(input("Number likh idhr: "))
if x<0:
    raise Exception("Sahi Number Likh: ")


# In[7]:


x= int(input("Number likh idhr: "))
if type(x) is int:
    raise TypeError("Type in String Format: ")


# In[8]:


x= int(input("Number likh idhr: "))
if not type(x) is int:
    raise TypeError("Type in String Format: ")


# In[ ]:




