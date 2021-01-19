#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

c = np.arange(0,2*np.pi,0.01)
plt.plot(c,np.sin(c))
plt.show()


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.01)
plt.plot(x,np.cos(x))
plt.show()


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.01)

plt.plot(x,np.cos(x)+ np.sin(x))
plt.show()


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.01)

plt.plot(x**2 +3)
plt.show()


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.01)

plt.plot(np.sqrt(x+4))
plt.show()


# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2,3,4,5,6,7,8,9,10])
b = np.array([2,4,6,8,10,12,14,16,18,20])

plt.plot(3*a**2 +b**2)
plt.show()


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.01)
a = np.array([1,3,6,9])
b = np.array([1,5,10,18])

plt.plot(np.sqrt(a**2 + b**2 +2*a*b))
plt.show()


# In[ ]:




