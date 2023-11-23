import numpy as np

a = [6, 2, 5, 0, 1, 3, 4, 7, 8, 9, 10, 11]
arr = np.array(a)
arr.shape = (3, 4)
print(arr)
b1 = arr[:2, :2]
b2 = arr[2]
b3 = arr[1:, 2:]
print(b1)
print(b2)
print(b3)
3
