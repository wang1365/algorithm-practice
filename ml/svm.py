from sklearn import svm
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
print type(iris), len(iris.data)


def test():
    XY = np.array(zip(iris.data, iris.target))
    np.random.shuffle(XY)
    X, Y = XY[:, :1][:100], XY[:, 1:][:100]
    X_test, Y_test = XY[:, :1][100:], XY[:, 1:][100:]
    X.shape, Y.shape = -1, -1
    X_test.shape, Y_test.shape = -1, -1
    X = np.asarray([list(i) for i in X])
    Y = np.asarray([int(i) for i in Y])
    X_test = [list(i) for i in X_test]
    print 'X:', X
    print 'Y:', Y
    print 'X:', X.shape
    print 'Y:', Y.shape

    m = svm.SVC(C=0.9)
    m.fit(X, Y)

    print 'Y_pre:', m.predict(X_test)
    print 'Y_test:', Y_test

if __name__ == '__main__':
    test()