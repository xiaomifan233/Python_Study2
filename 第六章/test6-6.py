import numpy as np
import matplotlib.pyplot as plt
#导入数据
Emp_data= np.loadtxt('Employedpopulation.csv',delimiter = ",", usecols=(1,2,3,4,5,6,7,8,9,10),dtype=int)

# 设置matplotlib正常显示中文和负号
plt.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
plt.rcParams['axes.unicode_minus']=False     # 正常显示负号

#创建一个绘图对象, 并设置对象的宽度和高度
plt.figure(figsize=(6, 4))
#绘制全部就业人员拆线图
line1 = plt.plot(Emp_data[0],Emp_data[1],"r-")
#绘制城镇就业人员拆线图
line2 = plt.plot(Emp_data[0],Emp_data[2],"g--")
#绘制乡村就业人员拆线图
line3 = plt.plot(Emp_data[0],Emp_data[3],"b-.")

plt.xlabel('年份')
plt.ylabel('人员(万人)')
plt.ylim((30000,80000))
plt.xlim(2006,2017)
plt.title("2007-2016年城镇、乡村和全部就业人员情况折线图")
#添加图例
plt.legend((line1,line2,line3),['全部就业','城镇就业','乡村就业'])
plt.savefig('Employedpopulation_line.png')
plt.show()