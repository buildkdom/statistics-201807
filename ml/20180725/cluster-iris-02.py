# 아래 링크가 도움이 될 것으로 보임
# http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_iris.html
import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn import datasets

# iris 데이터를 로드
iris = datasets.load_iris()
data = iris["data"]

# 학습 → 클러스터 생성
# model = cluster.KMeans(n_clusters=3)
model = cluster.KMeans()


#n_clusters =3 : 클러스터 개수 지정
model.fit(data)

# 학습 결과의 라벨 취득
labels = model.labels_

### 그래프 그리기
ldata = data[labels == 0]
plt.scatter(ldata[:, 2], ldata[:, 3],c='black' ,alpha=0.3,s=100 ,marker="o")

ldata = data[labels == 1]
plt.scatter(ldata[:, 2], ldata[:, 3],c='black' ,alpha=0.3,s=100 ,marker="^")

ldata = data[labels == 2]
plt.scatter(ldata[:, 2], ldata[:, 3],c='black' ,alpha=0.3,s=100 ,marker="*")

# 축 라벨의 설정
plt.xlabel(iris["feature_names"][2],fontsize='large')
plt.ylabel(iris["feature_names"][3],fontsize='large')


plt.show()