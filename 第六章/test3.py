import numpy as np
import matplotlib.pyplot as plt

Emp_data = np.loadtxt('全社会用电量-2016.csv', delimiter=",", usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                      dtype=float)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
plt.figure(figsize=(15, 10))
line1 = plt.bar(Emp_data[0], Emp_data[1],width = 0.35,color = 'red',edgecolor = 'white')
line2 = plt.bar(Emp_data[0]+0.35, Emp_data[3],width = 0.35,color = 'green',edgecolor = 'white')
line3 = plt.bar(Emp_data[0]+0.70, Emp_data[4],width = 0.35,color = 'blue',edgecolor = 'white')
line4 = plt.bar(Emp_data[0]+1.05, Emp_data[5],width = 0.35,color = 'yellow',edgecolor = 'white')
line5 = plt.bar(Emp_data[0]+1.40, Emp_data[2],width = 0.35,color = 'purple',edgecolor = 'white')
X = Emp_data[0]
Y1 = Emp_data[1]
for x, y in zip(X, Y1):
    plt.text(x + 0.3, y + 0.05, '%i' % y, ha='center')
Y2 = Emp_data[2]
for x, y in zip(X, Y2):
    plt.text(x + 0.6, y + 0.05, '%i' % y, ha='center')

Y3 = Emp_data[3]
for x, y in zip(X, Y3):
    plt.text(x + 0.9, y + 0.05, '%i' % y, ha='center')
Y4 = Emp_data[4]
for x, y in zip(X, Y4):
    plt.text(x + 1.2, y + 0.05, '%i' % y, ha='center')
Y5 = Emp_data[5]
for x, y in zip(X, Y5):
    plt.text(x + 1.5, y + 0.05, '%i' % y, ha='center')

plt.xlabel('月份')
plt.ylabel('度数')
plt.ylim((0, 200))
plt.xlim(0, 12)
plt.title("全社会用电量-2016情况散点图")
plt.legend({'全国用电', '第一产业', '第二产业', '第三产业', '城乡居民生活用电'})
plt.savefig('energy_z.png')
plt.show()
