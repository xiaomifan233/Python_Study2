import numpy as np
arr = np.arange(12).reshape((3,4))
#计算算术平均数
a = np.mean(arr)
b = np.mean(arr,axis=0)
c = np.mean(arr,axis=1)
print(a,b,c)
#计算标准差
a = np.std(arr)
b = np.std(arr,axis=0)
c = np.std(arr,axis=1)
print(a,b,c)
#计算方差
a = np.var(arr)
b = np.var(arr,axis=0)
c = np.var(arr,axis=1)
print(a,b,c)
