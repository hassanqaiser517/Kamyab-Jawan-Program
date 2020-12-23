#!/usr/bin/env python
# coding: utf-8

# In[5]:


class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = myclass("Hassan",17) #Object
print(p1.name)
print(p1.age)


# In[22]:


class myclass:
    def __init__(self, name):
        self.name = name
        
    def myfun(self):
        print("My name is "+ self.name)
        
p1= myclass("Hassan") #Object
p1.myfun()


# In[44]:


class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfun(self):
        print("My name is "+ self.name)
        print("I am "+ self.age + " years old")
        
        
p1= myclass("Hassan","17") #Object
p1.myfun()


# In[41]:


class person:
    def __init__(self, fname, lname):
        self.first= fname
        self.last= lname
    def printname(self):
        print("My First name is "+self.first+" and My Last name is "+self.last) #Using (+)
p1= person("Hassan","Qaiser") #Object
p1.printname()


# In[46]:


class person:
    def __init__(self, fname, lname):
        self.first= fname
        self.last= lname
    def printname(self):
        print("My First name is ",self.first," and My Last name is ",self.last) #Using (,)
p1= person("Hassan","Qaiser") #Object
p1.printname() 


# In[47]:


class person:
    def __init__(self, fname, lname):
        self.first= fname
        self.last= lname
    def printname(self):
        print(self.first,self.last)
class firefighter(person): #Using double
    pass
f1= firefighter("Hassan","Qasier") #Object
f1.printname()


# In[ ]:


class person:
    def __init__(self, fname, lname):
        self.first= fname
        self.last= lname
    def printname(self):
        print(self.first,self.last)
class firefighter(person): #Using double
    def __init__(self, fname, lname):
        person.__init__(self,fname,lname)
    def printname1(self):
        print(self.first,self.last)
obj1= firefighter("H","Q")
obj1.printname1


# In[ ]:





# In[ ]:




