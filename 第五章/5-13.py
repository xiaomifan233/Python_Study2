import numpy as np

a = np.repeat(7., 4)
arr = np.array([10, 20])
b = np.repeat(arr, [3, 2])

arr = np.array([[10, 20], [30, 40]])

c = np.repeat(arr, [3, 2], axis=0)

d = arr.repeat([3, 2], axis=1)

print('数据重复4次', a, '\n元素重复', b, '\n沿轴 0 重复数据',
      c, "\n沿轴 1 重复数据", d)
