import numpy as np
#创建数组arr
arr = np.array([3,7,5,6,8,9,7,2,6,2,5,9,10])

print('第1个数组：')
print(arr)

print('第1个数组的去重（唯一值）数组：')
arr_u = np.unique(arr)
print(arr_u)

print('去重数组的索引数组：')
u_index = np.unique(arr, return_index=True)
print(u_index)
print('原数组中的元素对应去重数组中的元素的索引值：')
print('原数组',arr)
print('用去重数组下标标记原数组中元素：')
arr_u,u_inverse = np.unique(arr, return_inverse=True)
print(u_inverse)

print('使用去重数组下标重构原数组：')
print(arr_u[u_inverse])

print('返回去重元素的重复数量：')
arr_u,u_inverse = np.unique(arr, return_counts=True)

print(u_inverse)