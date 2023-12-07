import numpy as np

arr = np.array([10, 20])

a = np.tile(arr, 2)

b = np.tile(arr, (3, 2))

c = np.tile(42.0, (3, 2))
print(a, '\n', b, '\n', c)
