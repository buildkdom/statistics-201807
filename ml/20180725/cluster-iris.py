from sklearn import datasets
from sklearn import metrics
iris = datasets.load_iris()
print (metrics.confusion_matrix(iris['target'], model.labels_))