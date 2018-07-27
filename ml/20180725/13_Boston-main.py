#-*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

import numpy
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# seed 값 설정
seed = 0
numpy.random.seed(seed)
'''
 [01]  CRIM	자치시(town) 별 1인당 범죄율
 [02]  ZN	25,000 평방피트를 초과하는 거주지역의 비율
 [03]  INDUS	비소매상업지역이 점유하고 있는 토지의 비율
 [04]  CHAS	찰스강에 대한 더미변수(강의 경계에 위치한 경우는 1, 아니면 0)
 [05]  NOX	10ppm 당 농축 일산화질소
 [06]  RM	주택 1가구당 평균 방의 개수
 [07]  AGE	1940년 이전에 건축된 소유주택의 비율
 [08]  DIS	5개의 보스턴 직업센터까지의 접근성 지수
 [09]  RAD	방사형 도로까지의 접근성 지수
 [10]  TAX	10,000 달러 당 재산세율
 [11]  PTRATIO	자치시(town)별 학생/교사 비율
 [12]  B	1000(Bk-0.63)^2, 여기서 Bk는 자치시별 흑인의 비율을 말함.
 [13]  LSTAT	모집단의 하위계층의 비율(%)
 [14]  MEDV	본인 소유의 주택가격(중앙값) (단위: $1,000)
'''
df = pd.read_csv("housing.csv",
                 delim_whitespace=True,
                 header=None)
# names=['1','2','3','4','5','6','7','8','9','10','11','12']

'''
print(df.info())
print(df.head())
'''
dataset = df.values
X = dataset[:,0:13]
Y = dataset[:,13] # MEDV	본인 소유의 주택가격(중앙값) (단위: $1,000)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

model = Sequential()
model.add(Dense(30, input_dim=13, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error',
              optimizer='adam')

model.fit(X_train, Y_train, epochs=200, batch_size=10)

# 예측 값과 실제 값의 비교
Y_prediction = model.predict(X_test).flatten()
for i in range(10):
    label = Y_test[i]
    prediction = Y_prediction[i]
    print("실제가격: {:.3f}, 예상가격: {:.3f}".format(label, prediction))

plt.figure(figsize=(13,13))
# visualize
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)
plt.show()