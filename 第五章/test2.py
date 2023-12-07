import numpy as np
import datetime
date = np.loadtxt('data_date.csv',dtype=np.str_,skiprows=1)
list1 = []
for i in date.tolist():
    y = int(i[6:10])
    m = int(i[3:5])
    d = int(i[0:2])
    a = datetime.date(y,m,d)
    week = a.isoweekday()
    list1.append(week)
print(list1)
arr_week = np.array(list1)
print(arr_week)