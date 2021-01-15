import numpy as np
import pandas as pd
df = pd.DataFrame(np.array([[1, 6, 2],
                            [2, np.nan, 1],
                            [np.nan, np.nan, 9]]))
df.columns = ['X', 'Y', 'Z']
print(df)

#Using fillna to fill Null Values
a = df.fillna("88")
print(a)

#Using dropna to drop Null Values
b = df.dropna()
print(b)
#giving Axis to it
b = df.dropna(axis=1)
print(b)