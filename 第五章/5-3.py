# -*- coding: utf-8 -*-
import numpy as np
arr = np.array([[0,3,1,5],[2,4,6,1],[2,8,9,2]])

#求arr数组的最大值
max1 = np.amax(arr)
print(max1)

#求arr数组的垂直方向最大值
max2 = np.amax(arr,axis=0)
print(max2)
#求arr数组的水平方向最大值
max3 = np.amax(arr,axis=1)
max4 = np.max(arr,axis=1)
print(max3,max4)

#amin函数与nanmin函数区别
arr = np.arange(5, dtype=float)
print(arr)                         # [0. 1. 2. 3. 4.]
arr[3] = np.nan
a = np.amin(arr)
print(a)                           # 用amin函数输出nan
b = np.nanmin(arr)
print(b)                           #用nanmin函数输出0.0