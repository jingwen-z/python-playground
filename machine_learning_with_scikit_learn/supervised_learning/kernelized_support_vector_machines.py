#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Introduction to Machine Learning with Python
Chapter 2
Supervised Learning - Kernelized Support Vector Machines
"""

import matplotlib.pyplot as plt
import mglearn.datasets
from mpl_toolkits import mplot3d
import numpy as np
from sklearn import datasets
from sklearn import model_selection
from sklearn import svm

"""
Linear models and nonlinear features
"""
x, y = datasets.make_blobs(centers=4, random_state=8)
y = y % 2

mglearn.discrete_scatter(x[:, 0], x[:, 1], y)
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')

linear_svm = svm.LinearSVC().fit(x, y)

# decision boundary found by a linear SVM
mglearn.plots.plot_2d_separator(linear_svm, x)
mglearn.discrete_scatter(x[:, 0], x[:, 1], y)
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')

# add a third feature derived from feature 1
x_new = np.hstack([x, x[:, 1:] ** 2])
figure = plt.figure()

ax = mplot3d.Axes3D(figure, elev=-152, azim=-26)
mask = y == 0

ax.scatter(x_new[mask, 0], x_new[mask, 1], x_new[mask, 2], c='b', cmap=mglearn.cm2, s=60)
ax.scatter(x_new[~mask, 0], x[~mask, 1], x_new[~mask, 2], c='r', marker='^', cmap=mglearn.cm2, s=60)
ax.set_xlabel('feature0')
ax.set_ylabel('feature1')
ax.set_zlabel('feature1 ** 2')

# decison boundary found by a linear SVM on the expanded three-dimensional dataset
linear_svm_3d = svm.LinearSVC().fit(x_new, y)
coef, intercept = linear_svm_3d.coef_.ravel(), linear_svm_3d.intercept_

figure_margin = plt.figure()
ax = mplot3d.Axes3D(figure_margin, elev=-152, azim=-26)
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

"""
Understanding SVMs
"""
x, y = mglearn.tools.make_handcrafted_dataset()
svm_rbf = svm.SVC(kernel='rbf', C=10, gamma=0.1).fit(x, y)
mglearn.plots.plot_2d_separator(svm_rbf, x, eps=.5)
mglearn.discrete_scatter(x[:, 0], x[:, 1], y)

# plot support vectors
sv = svm_rbf.support_vectors_

# class labels of support vectors are given by the sign of the dual coefficients
sv_labels = svm_rbf.dual_coef_.ravel() > 0
mglearn.discrete_scatter(sv[:, 0], sv[:, 1], sv_labels, s=15, markeredgewidth=3)
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')

"""
Tuning SVM parameters
"""
fig, axes = plt.subplots(3, 3, figsize=(15, 10))

for ax, c in zip(axes, [-1, 0, 3]):
    for a, gamma in zip(ax, range(-1, 2)):
        mglearn.plots.plot_svm(log_C=c, log_gamma=gamma, ax=a)

axes[0, 0].legend(['class 0', 'class 1', 'sv class 0', 'sv class 1'], ncol=4, loc=(.9, 1.2))
plt.show()

cancer = datasets.load_breast_cancer()
x_train, x_test, y_train, y_test = model_selection.train_test_split(cancer.data, cancer.target, random_state=0)

my_svc = svm.SVC()
my_svc.fit(x_train, y_train)
print('Accuracy on training set: {:.2f}'.format(my_svc.score(x_train, y_train)))
print('Accuracy on test set: {:.2f}'.format(my_svc.score(x_test, y_test)))

plt.plot(x_train.min(axis=0), 'o', label='min')
plt.plot(x_train.max(axis=0), '^', label='max')
plt.legend(loc=4)
plt.xlabel('Feature index')
plt.ylabel('Feature magnitude')
plt.yscale('log')
plt.show()

"""
Preprocessing data for SVMs
"""
# compute the minimum value per feature on the training set
min_on_training = x_train.min(axis=0)

# compute the range of each feature (max-min) on the training set
range_on_training = (x_train - min_on_training).max(axis=0)

# subtract the min and divide by range
x_train_scaled = (x_train - min_on_training) / range_on_training
print('Minimum for each feature\n{}'.format(x_train_scaled.min(axis=0)))
print('Maximum for each feature\n{}'.format(x_train_scaled.max(axis=0)))

x_test_scaled = (x_test - min_on_training) / range_on_training

my_svc.fit(x_train_scaled, y_train)
print('Accuracy on training set: {:.3f}'.format(my_svc.score(x_train_scaled, y_train)))
print('Accuracy on test set: {:.3f}'.format(my_svc.score(x_test_scaled, y_test)))

# change value of C
my_svc1000 = svm.SVC(C=1000)
my_svc1000.fit(x_train_scaled, y_train)
print('Accuracy on training set: {:.3f}'.format(my_svc1000.score(x_train_scaled, y_train)))
print('Accuracy on test set: {:.3f}'.format(my_svc1000.score(x_test_scaled, y_test)))
