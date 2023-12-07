import numpy as np


def lido_conv(x):
    keys = np.array(['', 'I', 'II', 'III', 'IIII', 'V', 'VI', 'VII', 'VIII',
                     'IX', 'X', 'XI', 'XII'])
    keys_list = keys.tolist()  # 将数组转换成列表

    a = str(x, encoding="UTF-8")  # 将二进制字符转换成字符
    # 使用NumPy的where函数，获得将罗马数字转换成对应的阿拉伯数字
    result = np.where(a in keys, keys_list.index(a), 0)
    return result


# 取出震级存入magnitude数组和烈度存入lido数组
magnitude = np.loadtxt('earthquakes.csv', delimiter=",", usecols=(5,), dtype=float, skiprows=1)
lido = np.loadtxt('earthquakes.csv', delimiter=",", usecols=(6,), dtype=np.int_, skiprows=1, converters={6: lido_conv})
print(magnitude, lido)

# 计算震级和烈度最大值、最小值、算术平均值和中位数
print("最大震级 =", np.max(magnitude))
print("最大震级 =", np.amax(magnitude))
print("最大烈度 =", np.max(lido))
print("最小震级 =", np.min(magnitude))
print("最小震级 =", np.amin(magnitude))
print("最小烈度 =", np.min(lido))
print("震级平均值 =", np.mean(magnitude))
print("烈度平均值 =", np.sum(lido) / np.count_nonzero(lido))

print("震级中位数 =", np.median(magnitude))
print("烈度中位数 =", np.median(lido))

# 统计不同震级发生次数
print('不同震级震级数组：', np.unique(magnitude))
print('不同震级发现次数：')
arr_u, u_inverse = np.unique(magnitude, return_counts=True)
print(u_inverse)

# 统计发生6级以上的震级次数总和
m_index = np.where(magnitude > 6)  # 震级大于6的元素的索引
m_sum = np.count_nonzero(m_index)
print(m_sum)

# 列出7，5级以上地震的发生日期、时间、经度、纬度和震级信息
arr = np.loadtxt('earthquakes.csv', delimiter=',',
                 dtype=np.string_, usecols=(0, 1, 2, 3), skiprows=1)
print('读取的地震数据：', arr)
cond = np.where(magnitude > 7.5)
print('7.5级以上地震的元素索引值：', cond)
print('使用元素索引值提取元素：')
print('7.5级以上地震数据:', arr[cond].astype(np.string_))
