# -*- coding: utf-8 -*-
import numpy as np

arr = np.arange(12).reshape(3, 4)
np.savetxt('test5-1-1.txt', arr)
np.savetxt('test5-1-2.txt', arr, fmt='%d', delimiter=',')
np.savetxt('test5-1-3.txt', arr, fmt='%s', delimiter=',', header=\
    'test5-1-3', footer='test5-1-3')
np.savetxt('test5-1-4.txt', arr, fmt='%d', delimiter=',', header=\
    'test5-1-4', comments='##')
np.savetxt('test5-1.csv', arr, fmt='%d', delimiter=',', header='test5-1')
