import numpy as np

a = np.random.rand()
print(a)
b = np.random.rand(1)
print(b)
c = np.random.rand(2, 3)
print(c)
a = np.random.randn()
print(a)
b = np.random.randn(1)
print(b)
c = np.random.randn(2, 3)
print(c)
a = np.random.randint(6)
print(a)
b = np.random.randint(6, size=1)
print(b)
c = np.random.randint(6, size=(2, 4), dtype='int64')
print(c)
a = np.random.random(6)
print(a)
b = np.random.random()
print(b)
