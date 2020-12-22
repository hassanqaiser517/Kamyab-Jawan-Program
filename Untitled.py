#!/usr/bin/env python
# coding: utf-8

# In[20]:


def myfunction(num1,num2,num3):
    max = numb1,num2,num3
num1= int(input("Enter Number = "))
num2= int(input("Enter Number = "))
num3= int(input("Enter Number = "))
print("Largest no. = ",max(num1,num2,num3))    


# In[2]:


def max_two(x,y):
    if x > y:
        return x
    return y
def max_three(x,y,z):
    return max_two(x, max_two(y,z))
print(max_three(15,25,49))


# In[ ]:




