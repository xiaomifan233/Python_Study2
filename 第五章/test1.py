import numpy as np

a = [6, 2, 5, 0, 1, 3, 4, 7, 8, 9]
b = ['2', 'a', '3', '1', 5, 7, 5.9]
arr_a = np.array(a)
print('第1个数组：', arr_a)
print('第1个数组的去重（去重后的值）数组：',np.unique(arr_a))
arr_b = np.array(b)
print('第2个数组：', arr_b)
print('第2个数组的去重（去重后的值）数组：',np.unique(arr_b))
print('返回去重后的值的重复数量：')
arr_a_u, u_a_inverse = np.unique(arr_a, return_counts=True)
print(u_a_inverse)
arr_b_u, u_b_inverse = np.unique(arr_b, return_counts=True)
print(u_b_inverse)