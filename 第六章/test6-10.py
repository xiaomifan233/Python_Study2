import matplotlib.pyplot as plt
import numpy as np

Emp_data = np.loadtxt('Employedpopulation.csv', delimiter=",", usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), dtype=int)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
X = [Emp_data[1], Emp_data[2], Emp_data[3]]
plt.figure(figsize=(8, 6))
label = ['全国就业', '城镇就业', '乡村就业']
plt.boxplot(X, notch=True, labels=label, meanline=True)
plt.title("2007-2016年城镇、乡村和全部就业人员情况箱线图")
plt.legend( {'全国就业', '城镇就业', '乡村就业'})
plt.savefig('Employedpopulation_box.png')
plt.show()
