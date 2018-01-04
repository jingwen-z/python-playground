#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Introduction to Machine Learning with Python
Chapter 2
Supervised Learning - Kernelized Support Vector Machines
"""

import matplotlib.pyplot as plt
import mglearn.datasets
from mpl_toolkits.mplot3d import Axes3D, axes3d
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import LinearSVC

"""
Linear models and nonlinear features
"""

x, y = make_blobs(centers=4, random_state=8)
y = y % 2

mglearn.discrete_scatter(x[:, 0], x[:, 1], y)
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')

linear_svm = LinearSVC().fit(x, y)

# decision boundary found by a linear SVM
mglearn.plots.plot_2d_separator(linear_svm, x)
mglearn.discrete_scatter(x[:, 0], x[:, 1], y)
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')

# add a third feature derived from feature 1
x_new = np.hstack([x, x[:, 1:] ** 2])
figure = plt.figure()

ax = Axes3D(figure, elev=-152, azim=-26)
mask = y == 0

ax.scatter(x_new[mask, 0], x_new[mask, 1], x_new[mask, 2], c='b', cmap=mglearn.cm2, s=60)
ax.scatter(x_new[~mask, 0], x[~mask, 1], x_new[~mask, 2], c='r', marker='^', cmap=mglearn.cm2, s=60)
ax.set_xlabel('feature0')
ax.set_ylabel('feature1')
ax.set_zlabel('feature1 ** 2')

# decison boundary found by a linear SVM on the expanded three-dimensional dataset
linear_svm_3d = LinearSVC().fit(x_new, y)
coef, intercept = linear_svm_3d.coef_.ravel(), linear_svm_3d.intercept_

figure_margin = plt.figure()
ax = Axes3D(figure_margin, elev=-152, azim=-26)
xx = np.linspace(x_new[:, 0].min() - 2, x_new[:, 0].max() + 2, 50)
yy = np.linspace(x_new[:, 1].min() - 2, x_new[:, 1].max() + 2, 50)

XX, YY = np.meshgrid(xx, yy)
ZZ = (coef[0] * XX + coef[1] * YY + intercept) / -coef[2]
ax.plot_surface(XX, YY, ZZ, rstride=8, cstride=8, alpha=0.3)
ax.scatter(x_new[mask, 0], x_new[mask, 1], x_new[mask, 2], c='b', cmap=mglearn.cm2, s=60)
ax.scatter(x_new[~mask, 0], x_new[~mask, 1], x_new[~mask, 2], c='r', marker='^', cmap=mglearn.cm2, s=60)
ax.set_xlabel('feature0')
ax.set_ylabel('feature1')
ax.set_zlabel('feature1 ** 2')

# decision boundary above as a function of the original two features
ZZ = YY ** 2
dec = linear_svm_3d.decision_function(np.c_[XX.ravel(), YY.ravel(), ZZ.ravel()])
plt.contourf(XX, YY, dec.reshape(XX.shape), levels=[dec.min(), 0, dec.max()], cmap=mglearn.cm2, alpha=0.5)
mglearn.discrete_scatter(x_new[:, 0], x_new[:, 1], y)

plt.xlabel('Feature 0')
plt.ylabel('Feature 1')

plt.show()
