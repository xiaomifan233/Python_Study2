import numpy as np

price, rating = np.loadtxt('Mobile.csv', delimiter=",", usecols=(1, 2), dtype=float, unpack=True)
print(price, rating)
u_price = np.unique(price)  # 获取价格表
print(u_price)
p_size = u_price.size  # 计算手机价格分类的数量
print(p_size)
price_rating = np.zeros((p_size, 5))
j = 0
for i in u_price:
    price_rating[j, 0] = i
    price_cond = np.where(price == i)
    print('满足某一价格条件的元素索引值：', price_cond)
    print('使用元素索引值提取评分元素：')
    m_rating = rating[price_cond].astype(np.int_)
    print('评分数组', m_rating)

    price_rating[j, 1] = np.max(m_rating)
    price_rating[j, 2] = np.min(m_rating)
    price_rating[j, 3] = np.mean(m_rating)
    price_rating[j, 4] = np.median(m_rating)

    print("最大评分 =", np.max(m_rating))
    print("最小评分 =", np.min(m_rating))
    print("评分平均值 =", np.mean(m_rating))
    print("评分中位数 =", np.median(m_rating))
    j += 1

print('输出按价格分类统计分析结果:', price_rating)
