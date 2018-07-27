import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(100, 1)
x = x * 4 - 2
y = 3 * x - 2

# 이 라인을 넣어서 종속변수를 더럽혀보자
y += np.random.randn(100, 1)

print ("length of x =", len(x))
print ("length of y =", len(y))

from sklearn import linear_model
model = linear_model.LinearRegression()
# print ("[1][1] Coefficient:", model.coef_)
# print ("[1][2] Intercept:", model.intercept_)

model.fit(x, y)
print ("[2][1] Coefficient:", model.coef_)
print ("[2][2] Intercept:", model.intercept_)
print ("[2][3] model(x,y) score", model.score(x, y))

plt.scatter(x, y, marker='+')
plt.scatter(x, model.predict(x), marker='o')
plt.show()