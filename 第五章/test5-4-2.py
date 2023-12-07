import numpy as np

# 加载Mobile.csv文件，以逗号分隔，取出第一列和第三列，分别赋值给brand和rating
# brand = np.loadtxt('Mobile.csv', delimiter=',', usecols=(0), dtype=str)
# rating = np.loadtxt('Mobile.csv', delimiter=',', usecols=(2), dtype=float)
brand, rating = np.loadtxt('Mobile.csv', delimiter=',', usecols=(0, 2), dtype=str, unpack=True)
# 获取brand中的唯一值，赋值给u_brand
u_brand = np.unique(brand)
# 打印u_brand
print(u_brand)
# 获取u_brand的长度，赋值给b_size
b_size = u_brand.size
# 打印b_size
print(b_size)
# 创建一个元素全为字符串的二维数组brand_rating，大小为b_size*5
brand_rating = np.zeros((b_size, 5)).astype(str)
j = 0
# 遍历品牌列表
for i in u_brand:
    # 将品牌列表中的品牌赋值给brand_rating
    brand_rating[j, 0] = i
    # 获取品牌在品牌列表中的索引值
    brand_code = np.where(brand == i)
    print('满足某一价格条件的元素索引值：', brand_code)
    print("使用元素索引值提取评分元素")
    # 将品牌在品牌列表中的索引值提取评分元素
    m_rating = rating[brand_code].astype(np.int_)
    print('评分数组', m_rating)

    # 计算品牌评分列表中的最大值
    brand_rating[j, 1] = np.max(m_rating)
    # 计算品牌评分列表中的最小值
    brand_rating[j, 2] = np.min(m_rating)
    # 计算品牌评分列表中的平均值
    brand_rating[j, 3] = np.mean(m_rating)
    # 计算品牌评分列表中的中位数
    brand_rating[j, 4] = np.median(m_rating)

    print("最大评分 =", np.max(m_rating))
    print("最小评分 =", np.min(m_rating))
    print("评分平均值 =", np.mean(m_rating))
    print("评分中位数 =", np.median(m_rating))

    j += 1
# np.save('1',brand_rating)
np.set_printoptions(threshold=1e6)
print(brand_rating)
