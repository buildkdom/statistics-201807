#-*- coding: utf-8 -*-
import numpy
import pandas

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

# seed 값 설정
seed = 0
numpy.random.seed(seed)

df = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)
'''
print(df.info())
print(df.head())
'''
dataset = df.values
X = dataset[:,0:13] # 주택가격을 제외한 모든 독립변수 값 array들
Y = dataset[:,13] # 주택가격

print(len(X[1]), X[1])
print(len(Y))