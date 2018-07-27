from keras.datasets import mnist
from keras.utils import np_utils
import matplotlib.pyplot as plt
import sys
import numpy

def imageToMatrix(img):
    for x in img:
        for i in x:
            sys.stdout.write('%d\t' % i)
        sys.stdout.write('\n')

def drawImage(img):
    plt.imshow(img, cmap='Greys')
    plt.show()

#
# load mnist dataset
#
(X_train, Y_class_train), (X_test, Y_class_test) = mnist.load_data()

print ("number of training images: %d" % X_train.shape[0])
print ("number of testing images: %d" % X_test.shape[0])

#
# check the each values
#
# imageToMatrix(X_train[0])

# drawImage(X_train[0])
# drawImage(X_train[1])
# drawImage(X_train[2])

# print ("class : %d, %d, %d" % (Y_class_train[0],
#                                Y_class_train[1],
#                                Y_class_train[2]))


X_train = X_train.reshape(X_train.shape[0], 784)
X_train = X_train.astype('float64')
X_train = X_train / 255

X_test = X_test.reshape(X_test.shape[0], 784).astype('float64') / 255
print ("[변환전] class : %d" % (Y_class_train[0]))

# 바이너리화 과정
Y_train = np_utils.to_categorical(Y_class_train, 10)
Y_test = np_utils.to_categorical(Y_class_test, 10)

print ("[변환후] class :", Y_train[0])