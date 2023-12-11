import matplotlib.pyplot as plt
import numpy as np
Emp_title = np.loadtxt('全社会用电量-2016.csv',delimiter=",",usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),dtype=str)
Emp_data = np.loadtxt('全社会用电量-2016.csv', delimiter=",", usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),skiprows=1,
                      dtype=np.float_)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
X = [Emp_data[0], Emp_data[1], Emp_data[2],Emp_data[3],Emp_data[4]]
plt.figure(figsize=(8, 6))
label = ['全国用电', '第一产业', '第二产业', '第三产业', '城乡居民生活用电']
plt.boxplot(X, notch=True, labels=label, meanline=True)
plt.title("全社会用电量-2016情况箱线图")
plt.legend( {'全国用电', '第一产业', '第二产业', '第三产业', '城乡居民生活用电'})
plt.savefig('energy_x.png')
plt.show()
