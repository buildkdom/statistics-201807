from sklearn import datasets
iris = datasets.load_iris()
#print (iris['DESCR'])
#print (iris['data'])
#print (iris['target'])
print (iris['target_names'])
print ("데이터 속성 개수("+ str(len(iris['feature_names']))+")", iris['feature_names'])