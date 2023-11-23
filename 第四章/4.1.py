import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
print('维度',arr1.ndim)
print('形状',arr1.shape)
print('元素总数',arr1.size)
print('数据类型',arr1.dtype)
print('每个元素的大小',arr1.itemsize)
arr1.shape=(3,2)
print(arr1)
