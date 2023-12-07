import numpy as np
k = ('name', 'age', 'tel')
v =  ('李明',  '21',  '13871234456')
ind = np.lexsort((k,v))
print  ('调用 lexsort() 函数：',ind)

print  ('使用这个索引来获取排序后的数据：')
print  ([k[i]  +  ", "  + v[i]  for i in ind])