import numpy as np
import matplotlib.pyplot as plt

Emp_data = np.loadtxt('Employedpopulation.csv', delimiter=",", usecols=(1), dtype=int)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

X = [Emp_data[2], Emp_data[3]]

plt.figure(figsize=(8, 8))
label = ['城镇就业', '乡村就业']
explode = [0.01, 0.01]

plt.pie(X, explode=explode, labels=label, autopct='%1.2f%%')
plt.title("2016年城镇和乡村就业人员情况饼图")
plt.legend({'城镇就业', '乡村就业'})
plt.savefig('Employedpopulation_pie.png')
plt.show()
