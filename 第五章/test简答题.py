'''
1. 在NumPy中，读取TXT文件和CSV格式文件的函数是loadtxt();通过指定usecols参数
2. 在NumPy中，读取TXT文件和CSV格式文件的函数是loadtxt();通过指定unpack参数，如果True，读入属性将分别写入不同变量。
3．在NumPy中，读取TXT文件和CSV格式文件的函数是loadtxt();通过指定converters参数来实现将文本文件中数据列和转换函数之间联系在一起。
4．在NumPy中，savez()函数能提供将多个数组存储至一个文件的能力。
5．在NumPy中，savez()函数保存之后后缀名npz，使用解压程序打开npz文件可以看到里面是若干个以“数组名称”命名的npy格式的文件，数组名称默认为
   “arr_数字”的形式，在savez()函数中可以通过指明函数的参数名称来命名数组。
6．作用与区别：在NumPy中，求数组最大值的函数是amax()和nanmax()，其中，amax()函数是返回一个数组的最大值或者是沿轴返回
   数组的最大值。nanmax()函数是返回忽略任何NaN的数组的最大值或者是沿轴返回忽略任何NaN的数组的最大值。
7．在NumPy中，直接排序常用是sort()函数，而间接排序常用是argsort()函数和lexsort()函数。
   argsort()函数作用是对输入数组沿着给定轴执行间接排序，并根据指定排序类型返回数据的索引数组。使用该索引数组可以获得排序数据。
   lexsort()函数使用键序列执行间接排序，键可以看作是电子表格中的一列，最后一个键是排序的主键，该函数返回一个索引数组。使用该索引数组可以获得排序数据。
'''