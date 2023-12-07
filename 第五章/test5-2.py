import numpy as np
import os

arr1 = np.loadtxt('test5-1-1.txt')
print(arr1)
arr2 = np.loadtxt('test5-1-2.txt', delimiter=',')
arr3 = np.loadtxt('test5-1-3.txt', dtype=np.int32, delimiter=',')
arr4 = np.loadtxt('test5-1-4.txt', delimiter=',')
print(arr2, arr3, arr4)
arr5 = np.loadtxt('test5-1.csv', delimiter=',')
arr6 = np.loadtxt('phone.csv', dtype=np.str_, delimiter=',',encoding='utf-8')
print(arr5, arr6)