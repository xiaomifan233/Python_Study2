import pandas as pd
import numpy as np


se1 = pd.Series([2,4,-3,7])
print(se1)
se2 = pd.Series([2,4,-3,7], index=['b','c','a','d'])
print(se2)
arr = np.array([2,3,4,5])
se3 = pd.Series(arr)
print(se3)
