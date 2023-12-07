import numpy as np
import matplotlib.pyplot as plt
Emp_data= np.loadtxt('Employedpopulation.csv',delimiter = ",",usecols=(1,2,3,4,5,6,7,8,9,10),dtype=int)
print(Emp_data)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(6, 4))
line1 = plt.scatter(Emp_data[0],Emp_data[1],c='r',marker='o')
line2 = plt.scatter(Emp_data[0],Emp_data[2],c='g',marker='x')
line3 = plt.scatter(Emp_data[0],Emp_data[3],c='b',marker='v')
plt.xlabel('年份')
plt.ylabel('人员(万人)')
plt.ylim((30000,80000))
plt.xlim(2006,2017)
plt.title("2007-2016年城镇、乡村和全部就业人员情况散点图")
plt.legend((line1,line2,line3),['全部就业','城镇就业','乡村就业'])
plt.savefig('Employedpopulation_s.png')
plt.show()
