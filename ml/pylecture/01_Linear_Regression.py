# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()


# x 값과 y값
x=[ 2,  4,  6,  8]
y=[81, 93, 91, 97]
# ax = fig.add_subplot(len(x), len(y), 1)
plt.scatter( x, y, label='scatter' )

# x와 y의 평균값
mx = np.mean(x)
my = np.mean(y)
print("x의 평균값:", mx)
print("y의 평균값:", my)

# 기울기 공식의 분모
divisor = sum([(mx - i)**2 for i in x])

# 기울기 공식의 분자
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d
dividend = top(x, mx, y, my)

print("분모:", divisor)
print("분자:", dividend)

# 기울기와 y 절편 구하기
a = dividend / divisor
b = my - (mx*a)

# 출력으로 확인
print("[1] 기울기 a =", a)
print("[2] y 절편 b =", b)

# print ([for i in x])

# plt.plot(a, predict, 'ro')

plt.grid(True)
plt.show()