#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = np.array([2, 4, 6, 8])
b = np.array([6, 3, 8, 1])

plt.plot(a, b)
plt.show()


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = np.array([2, 4, 6, 8])
b = np.array([6, 3, 8, 1])

plt.plot(a,b, marker = '.', ms=12,mec='k',mfc='r')
plt.plot(a, b)
plt.show()


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = np.array([5,3,7,4])
b = np.array([6, 1, 8, 2])

plt.plot(a, marker = '.', ms=15,mec='k',mfc='b')
plt.plot(b)
plt.show()


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = np.array([5,3,7,4])
b = np.array([6, 1, 8, 1])

plt.plot(a, marker = '.', ms=12,mec='k',mfc='r')
plt.plot(b)

c = np.arange(0,2*np.pi,0.01)
plt.plot(c,np.sin(c))
plt.show()


# In[ ]:




