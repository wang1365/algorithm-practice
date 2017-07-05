# coding: utf8
# 在scikit-learn中，提供了3中朴素贝叶斯分类算法：GaussianNB(高斯朴素贝叶斯)、MultinomialNB(多项式朴素贝叶斯)、BernoulliNB(伯努利朴素贝叶斯)

import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

X = np.asarray([[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [1, 1], [2, 2], [3, 3]])
y = np.asarray([1, 1, 1, 1, 1, 2, 2, 2])
clf = GaussianNB()
clf.class_prior_ = [0.675, 0.325]
clf.fit(X, y)

print clf.predict([[-1, -1], [2,3]])

