#!/usr/bin/env python
# coding: utf-8

# In[4]:


def max_two(x,y):
    if x > y:
        return x
    return y
def max_three(x,y,z):
    return max_two(x, max_two(y,z))
print(max_three(15,25,49))


# In[ ]:




