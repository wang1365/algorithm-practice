from random import shuffle

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
print type(iris), len(iris.data)


def test1():
    XY = np.array(zip(iris.data, iris.target))
    np.random.shuffle(XY)
    X, Y = XY[:, :1][:100], XY[:, 1:][:100]
    X_test, Y_test = XY[:, :1][100:], XY[:, 1:][100:]
    X.shape, Y.shape = -1, -1
    X_test.shape, Y_test.shape = -1, -1
    X = [list(i) for i in X]
    X_test = [list(i) for i in X_test]
    print 'X:', X
    print 'Y:', Y

    # Train model
    rf = RandomForestRegressor()
    rf.fit(X, Y)

    # Predict new sample
    Y_pre = rf.predict(X_test)
    print 'Y_test:', Y_test
    print 'Y_pre:', Y_pre


def test2():
    from sklearn.cross_validation import cross_val_score, ShuffleSplit
    X, Y, names = iris.data, iris.target, iris['feature_names']

    rf = RandomForestRegressor()
    scores = []
    for i in range(X.shape[1]):
        score = cross_val_score(rf, X[:, i:i + 1], Y,
                                scoring='r2',
                                cv=ShuffleSplit(len(X), 3, .3))
        scores.append((round(np.mean(score), 3), names[i]))
    print sorted(scores, reverse=True)


if __name__ == '__main__':
    test1()
    test2()
