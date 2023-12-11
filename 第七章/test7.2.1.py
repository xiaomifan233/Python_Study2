import numpy as np
import pandas as pd

dt = {'name': ['张艳', '李明', '王勇'], 'sex': ['False', 'True', 'True'], 'age': [18, 20, 19]}
df = pd.DataFrame(dt)
print(df)
df = pd.DataFrame(dt, columns=['name', 'age'])
print(df)
df = pd.DataFrame(dt, index=['a', 'b', 'c'], columns=['name', 'age'])
print(df)
dt = {'name': {'a': '张艳', 'b': '李明', 'c': '王勇'}, 'age': {'a': 18, 'b': 20}}
df = pd.DataFrame(dt)
print(df)
df = pd.DataFrame(np.arange(8).reshape(2, 4))
print(df)
