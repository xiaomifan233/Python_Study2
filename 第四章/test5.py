import numpy as np

a = [6, 2, 5, 0, 1, 3, 4, 7, 8, 9, 10, 11]
arr = np.array(a)
arr.shape = (4, 3)
b = arr[(1, 1, 2, 2), (1, 2, 1, 2)]
# Aprint(arr[1:3,1:4])
b.shape = (2, 2)
print(b)
