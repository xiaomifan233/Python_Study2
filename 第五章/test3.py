import numpy as np
a = [1.1,3.3,5.5,7.7,9.9]
b = [0.0,2.2,4.4,6.6,8.8]
arr_a = np.array(a)
print(arr_a)
c1 = arr_a[arr_a>6]
c2 = arr_a[arr_a<3]
arr_b = np.array(b)
c3 = arr_b[1:3]
print(c1,c2,c3)
c = np.concatenate((c2,c3,c1))
print(c)