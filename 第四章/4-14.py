import numpy as np

arr = np.arange(16).reshape(4, 4)
print('第1个数组arr：', arr)
print('未传递axis参数,在删除之前输入数组会被展开。')
print(np.delete(arr, [6, 9, 12]))
print(arr)
print('删除第3列：')
print(np.delete(arr, 2, axis=1))
print('删除第2行：')
print(np.delete(arr, 1, axis=0))
print('从数组中删除用切片表示元素范围值：')
print(np.delete(arr, np.s_[::2]))
