# -*- coding: utf-8 -*-
import numpy as np

# 使用字符串创建矩阵
str = '1 2 3;4 5 6;7 8 9'
a = np.mat(str)
a[1, 1] = 11  # 修改a矩阵1行1列值，不会影响str
print('用字符串创建矩阵:', a, str)  # 观察str输出没有变化

# 使用嵌套序列创建矩阵
b = np.mat([[2, 4, 6, 8], [1.0, 3, 5, 7.0]])
print('用嵌套序列创建矩阵:', b)

# 使用一个数组创建矩阵
arr = np.arange(9).reshape(3, 3)  # 创建3行3列数组
c = np.mat(arr)
c[1, 1] = 55  # 修改c矩阵1行1列值，arr值也跟着变化
print('数组创建矩阵:', c, arr)

# 使用matrix函数创建矩阵
c = np.matrix(arr, dtype=np.float_)  # 用arr数组创建矩阵
c[1, 1] = 66  # 修改c矩阵1行1列值，arr值不变化
d = np.matrix([[2, 4, 6, 8], [1.0, 3, 5, 7.0]], dtype=np.int64)  # 用序列创建矩阵
e = np.matrix('1 2 3;4 5 6;7 8 9', dtype=np.str_)  # 用字符串创建矩阵
f = np.matrix(a, dtype=np.str_)  # 用matrix对象创建矩阵
print('用matrix函数创建矩阵', c, arr, d, e, f)

# 使用bmat函数创建矩阵
a = np.mat('3 3 3;4 4 4')
b = np.mat('1 1 1;2 2 2')
print('用bmat函数创建矩阵:', np.bmat('a b; b a'))
