#!/usr/bin/env python
# coding: utf-8

# In[1]:


class playstation5:
    def __init__(self):
        self.__maxprice = 50000
        
    def PrintSell(self):
        print("Selling Price: {}".format(self.__maxprice))
    
    def setMaxPrice(self,price):
        self.__maxprice = price
        
#calling function Now    
PS5 = playstation5()
PS5.PrintSell()

#change price Now
PS5.__maxprice = 60000
PS5.PrintSell()

#Using Set Function
PS5.setMaxPrice(60000)
PS5.PrintSell


# In[ ]:




