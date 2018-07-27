from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.set_random_seed(seed)

# 데이터 입력
df = pd.read_csv('./dataset/sonar.csv', header=None)
'''
# 데이터 개괄 보기
print(df.info())

# 데이터의 일부분 미리 보기
print(df.head())
'''
dataset = df.values
X = dataset[:,0:60]
Y_obj = dataset[:,60]

# 문자열 변환 ('R' -> 1, 'M' -> 0)
e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)


# 학습 셋과 테스트 셋의 구분
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

model = Sequential()
model.add(Dense(24,  input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(loss='mean_squared_error',
            optimizer='adam',
            metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=130, batch_size=5)
# [1] model.fit(X_train, Y_train, epochs=130, batch_size=5) --> Test Accuracy 0.82
# [2] model.fit(X_train, Y_train, epochs=200, batch_size=5) --> Test Accuracy 0.8095
# [3] model.fit(X_train, Y_train, epochs=130, batch_size=5) --> Test Accuracy: 0.8254

# 테스트셋에 모델 적용
print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))
