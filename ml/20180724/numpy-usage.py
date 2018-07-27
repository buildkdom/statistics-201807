import matplotlib.pyplot as plt
import numpy as np
# numpy.random.normal : 정규분포 확률 밀도에서 표본을 추출하되, 아래의 parameter으로 세부 설정이 가능
# loc: 정규분포의 평균,  scale: 표준편차
mean = 0
std = 1
a1 = np.random.normal(mean, std, (2, 3))

# print ("extracted sample:", a1)
# plt.hist(a1)
# plt.show()

#
a2 = np.random.normal(0, 1, 10000)
plt.hist(a2, bins=100)
plt.show()