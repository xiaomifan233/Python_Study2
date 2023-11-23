import numpy as np


arr = np.arange(9).reshape(3,3)
print('原数组：',arr)
print('将arr数组转换成列表')
arr_list = arr.tolist()
print(arr_list)
arr_a = np.arange(4)
arr_b = np.array([0,1,1,0])
print('两个相同形状数组arr_a,arr_b相加:')
arr_c = arr_a + arr_b
print(arr_c,'=',arr_a,'+',arr_b)
print('两个相同形状数组arr_a,arr_b相减:')
arr_c = arr_a - arr_b
print(arr_c,'=',arr_a,'-',arr_b)
print('两个相同形状数组arr_a,arr_b相乘:')
arr_c = arr_a * arr_b
print(arr_c,'=',arr_a,'*',arr_b)
print(np.multiply(arr_a,arr_b))
print('两个相同形状数组arr_a,arr_b相除:')
print('数组arr_a相反数:')
print(-arr_a)
print('数组arr_a的平方:')
print(arr_a**2)
print('数组arr_a的按位异或:')
print(arr_a^2)
