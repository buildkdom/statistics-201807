import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.rand(100, 1)
x1 = x1 * 4 - 2 # -2~2

x2 = np.random.rand(100, 1)
x2 = x2 * 4 - 2 # -2~2

y = 3*x1 - 2*x2 + 1
y += np.random.randn(100, 1)

# training
from sklearn import linear_model
x1_x2 = np.c_[x1, x2]
print (x1_x2)
model = linear_model.LinearRegression()
model.fit(x1_x2, y)

#
print ("[2][1] Coefficient:", model.coef_)
print ("[2][2] Intercept:", model.intercept_)
print ("[2][3] model(x1_x2,y) score", model.score(x1_x2, y))

y_ = model.predict(x1_x2)

plt.subplot(1, 2, 1)
plt.scatter( x1, y, marker='+')
plt.scatter( x1, y_, marker='o')
plt.xlabel('x1')
plt.ylabel('y')

plt.subplot(1, 2, 2)
plt.scatter( x2, y, marker='+')
plt.scatter( x2, y_, marker='o')
plt.xlabel('x2')
plt.ylabel('y')

plt.tight_layout()
plt.show()