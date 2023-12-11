# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
#导入数据
Emp_data= np.loadtxt('Employedpopulation.csv',delimiter = ",",
                     usecols=(1,2,3,4,5,6,7,8,9,10),dtype=int)

# 设置matplotlib正常显示中文和负号
plt.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
plt.rcParams['axes.unicode_minus']=False     # 正常显示负号

#创建一个绘图对象, 并设置对象的宽度和高度
plt.figure(figsize=(8, 4))
#绘制全部就业人员柱状图
plt.bar(Emp_data[0],Emp_data[1],     width = 0.35,color = 'red',edgecolor = 'white')
#绘制城镇就业人员柱状图
plt.bar(Emp_data[0]+0.35,Emp_data[2],width = 0.35,color = 'green',edgecolor = 'white')
#绘制乡村就业人员柱状图
plt.bar(Emp_data[0]+0.7,Emp_data[3], width = 0.35,color = 'blue',edgecolor = 'white')
# 给图加text
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

plt.xlabel('年份')
plt.ylabel('人员(万人)')
plt.ylim((30000,80000))
plt.xlim(2006,2017)
plt.title("2007-2016年城镇、乡村和全部就业人员情况柱状图")
#添加图例
plt.legend({'全部就业','城镇就业','乡村就业'})
plt.savefig('Employedpopulation_bar.png')
plt.show()
