import numpy as np
arr = np.array([[4,5,3],[8,1,7]])
print('原数组\n',arr)

#调用 sort() 函数
a = np.sort(arr)
print('sort()函数排序\n',a)
#沿轴 0 排序
b = np.sort(arr,axis=0)
print('沿轴 0 排序\n',b)
#沿轴 1 排序
c = np.sort(arr,axis=1)
print('沿轴 1 排序\n',c)
# 在 sort 函数中排序字段
dt = np.dtype([('name',np.str_,10),('age',int)])
arr = np.array([("李明",19),("王力",21),("张艳",18)],dtype = dt)
print ('自定义的数组是：\n',arr)
print('按 name 排序：')
print(np.sort(arr,order='name'))