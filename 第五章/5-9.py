import numpy as np
arr = np.array([4,5,3,8,7])
print('原数组',arr)
a = np.argsort(arr)
print('调用argsort()函数',a)
print('用循环输出排序数组')
print(arr[a])