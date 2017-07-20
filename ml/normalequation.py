import numpy as np

X = [[0, 1, 3], [1, 2, 3], [4, 5, 6], [1, 4, 5]]
y = [11, 14, 31, 24]


def fun(x1, x2, x3):
    return x1 + 2 * x2 + 3 * x3


X = np.asmatrix(X)
y = np.asmatrix(y).T

# Normal Equation: (XT * X)**-1  * XT * y
ne = (X.T.dot(X) ** -1) * X.T * y
print(ne)

print(fun(1, 2, 3))
print(1 * ne[0][0] + 2 * ne[1][0] + 3 * ne[2][0])
