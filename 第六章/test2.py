import numpy as np
import matplotlib.pyplot as plt

Emp_data = np.loadtxt('全社会用电量-2016.csv', delimiter=",", usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                      dtype=float)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
plt.figure(figsize=(10, 10))
plt.plot(Emp_data[0], Emp_data[1],"r-")
plt.plot(Emp_data[0], Emp_data[3],"g--")
plt.plot(Emp_data[0], Emp_data[4],"b-.")
plt.plot(Emp_data[0], Emp_data[5],"y-")
plt.plot(Emp_data[0], Emp_data[2],"c.-")
plt.xlabel('月份')
plt.ylabel('度数')
plt.ylim((0, 200))
plt.xlim(0, 12)
plt.title("全社会用电量-2016情况散点图")
plt.legend({'全国用电', '第一产业', '第二产业', '第三产业', '城乡居民生活用电'})
plt.savefig('energy_z.png')
plt.show()