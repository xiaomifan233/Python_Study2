import numpy as np

ma = np.mat([[6, 4, 2, 8], [2.0, 1, 5, 7.0]])
mb = np.mat(np.arange(9).reshape(3, 3))
mc = np.mat(np.arange(8).reshape(2, 4))
print('矩阵相加：', ma + mc)
print('矩阵相减：', ma - mc)
print('矩阵相除：', mc / ma)
print('矩阵相乘：', ma, mc.T, ma * mc.T)
print('矩阵点乘:', np.multiply(ma, mc))
arr = np.array([[2, 4, 6, 8], [1.0, 3, 5, 7.0]])
ma[0]
print('取矩阵ma第1行值', ma[0])
ma[1, 1]
print(ma[1, 1])
arr[1][1]
print(arr[1][1])
# ma[1][1]
ma.shape
ma.shape[0]
ma.shape[1]
ma[0, :]
print(ma[0, :])
ma[0, 1:2]
print(ma[0, 1:2])
ma.sort()
print(ma)
list = [1, 2, 3, 5, 6]
np.mat(list)
print(np.mat(list))
