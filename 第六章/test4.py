import numpy as np
import matplotlib.pyplot as plt

Emp_data = np.loadtxt('全社会用电量-2016.csv', delimiter=",", usecols=(1), dtype=np.float_)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
X = [Emp_data[2], Emp_data[3], Emp_data[4], Emp_data[5]]
plt.figure(figsize=(8, 8))
label = ['第一产业', '第二产业', '第三产业', '城乡居民生活用电']
explode = [0.01, 0.01, 0.01, 0.01]

plt.pie(X, explode=explode, labels=label)
plt.title("全社会用电量-2016，一月饼状图")
plt.legend({'第一产业', '第二产业', '第三产业', '城乡居民生活用电'})
plt.savefig('energy_b.png')
plt.show()
