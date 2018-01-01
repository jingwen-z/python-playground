#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Introduction to Machine Learning with Python
Chapter 2
Supervised Learning
"""

import matplotlib.pyplot as plt
import mglearn.datasets
import numpy as np
from sklearn.datasets import load_boston
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import make_blobs
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

"""
Some sample datasets
"""
x, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(x, y, 'o')
plt.ylim(-3, 3)
plt.xlabel('Feature')
plt.ylabel('Target')

boston = load_boston()
print('Data shape: {}'.format(boston.data.shape))
x, y = mglearn.datasets.load_extended_boston()
print('x.shape: {}'.format(x.shape))

x, y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(x[:, 0], x[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First feature")
plt.ylabel("Second feature")
print("x.shape: {}".format(x.shape))

"""
Linear models for regression
"""
mglearn.plots.plot_linear_regression_wave()

"""
Linear regression (OLS)
"""
x, y = mglearn.datasets.make_wave(n_samples=60)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)

lr = LinearRegression().fit(x_train, y_train)
print('lr.coef_: {}'.format(lr.coef_))
print('lr.intercept_: {}'.format(lr.intercept_))

print('Training set score: {:.2f}'.format(lr.score(x_train, y_train)))
print('Test set score: {:.2f}'.format(lr.score(x_test, y_test)))

x, y = mglearn.datasets.load_extended_boston()
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

lr = LinearRegression().fit(x_train, y_train)
print('Training set score: {:.2f}'.format(lr.score(x_train, y_train)))
print('Test set score: {:.2f}'.format(lr.score(x_test, y_test)))

"""
Ridge regression
"""
# alpha = 1
ridge = Ridge().fit(x_train, y_train)
print('Training set score: {:.2f}'.format(ridge.score(x_train, y_train)))
print('Test set score: {:.2f}'.format(ridge.score(x_test, y_test)))

# alpha = 10
ridge10 = Ridge(alpha=10).fit(x_train, y_train)
print('Training set score: {:.2f}'.format(ridge10.score(x_train, y_train)))
print('Test set score: {:.2f}'.format(ridge10.score(x_test, y_test)))

# alpha = 0.1
ridge01 = Ridge(alpha=0.1).fit(x_train, y_train)
print('Training set score: {:.2f}'.format(ridge01.score(x_train, y_train)))
print('Test set score: {:.2f}'.format(ridge01.score(x_test, y_test)))

# compare coefficient magnitudes
plt.plot(ridge.coef_, 's', label='Ridge alpha=1')
plt.plot(ridge10.coef_, '^', label='Ridge alpha=10')
plt.plot(ridge01.coef_, 'v', label='Ridge alpha=0.1')
plt.plot(lr.coef_, 'o', label='Linear regression')

plt.xlabel('Coefficient index')
plt.ylabel('Coefficient magnitude')
plt.hlines(0, 0, len(lr.coef_))
plt.ylim(-25, 25)
plt.legend()
plt.show()

# learning curves for ridge regression and linear regression
mglearn.plots.plot_ridge_n_samples()
plt.show()

"""
Lasso
"""
# alpha = 1
lasso = Lasso().fit(x_train, y_train)
print('Training set score: {:.2f}'.format(lasso.score(x_train, y_train)))
print('Test set score: {:.2f}'.format(lasso.score(x_test, y_test)))
print('Number of features used: {}'.format(np.sum(lasso.coef_ != 0)))

# alpha = 0.01
lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(x_train, y_train)
print('Training set score: {:.2f}'.format(lasso001.score(x_train, y_train)))
print('Test set score: {:.2f}'.format(lasso001.score(x_test, y_test)))
print('Number of features used: {}'.format(np.sum(lasso001.coef_ != 0)))

# alpha = 0.0001
lasso00001 = Lasso(alpha=0.0001, max_iter=100000).fit(x_train, y_train)
print('Training set score: {:.2f}'.format(lasso00001.score(x_train, y_train)))
print('Test set score: {:.2f}'.format(lasso00001.score(x_test, y_test)))
print('Number of features used: {}'.format(np.sum(lasso00001.coef_ != 0)))

# compare coefficient magnitudes
plt.plot(lasso.coef_, 's', label='Lasso alpha=1')
plt.plot(lasso001.coef_, '^', label='Lasso alpha=0.01')
plt.plot(lasso00001.coef_, 'v', label='Lasso alpha=0.0001')
plt.plot(ridge01.coef_, 'o', label='Lasso alpha=0.1')

plt.xlabel('Coefficient index')
plt.ylabel('Coefficient magnitude')
plt.ylim(-25, 25)
plt.legend(ncol=2, loc=(0, 1.05))
plt.show()

"""
Linear models for classification
"""
x, y = mglearn.datasets.make_forge()
fig, axes = plt.subplots(1, 2, figsize=(10, 3))

for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
    clf = model.fit(x, y)
    mglearn.plots.plot_2d_separator(clf, x, fill=False, eps=0.5, ax=ax, alpha=.7)
    mglearn.discrete_scatter(x[:, 0], x[:, 1], y, ax=ax)
    ax.set_title("{}".format(clf.__class__.__name__))
    ax.set_xlabel("Feature 0")
    ax.set_ylabel("Feature 1")
axes[0].legend()

# decision boundaries of a linear SVM on the forge dataset for different values of C
mglearn.plots.plot_linear_svc_regularization()

# analyse LinearLogistic
cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
logreg = LogisticRegression().fit(x_train, y_train)
print('Training set score: {:.3f}'.format(logreg.score(x_train, y_train)))
print('Test set score: {:.3f}'.format(logreg.score(x_test, y_test)))

logreg100 = LogisticRegression(C=100).fit(x_train, y_train)
print('Training set score: {:.3f}'.format(logreg100.score(x_train, y_train)))
print('Test set score: {:.3f}'.format(logreg100.score(x_test, y_test)))

logreg001 = LogisticRegression(C=0.01).fit(x_train, y_train)
print('Training set score: {:.3f}'.format(logreg001.score(x_train, y_train)))
print('Test set score: {:.3f}'.format(logreg001.score(x_test, y_test)))

print('logreg001.score:\n', logreg001.score)

# coefficients learnt by logistic regression
plt.plot(logreg.coef_.T, 'o', label='C=1')
plt.plot(logreg100.coef_.T, '^', label='C=100')
plt.plot(logreg001.coef_.T, 'v', label='C=0.01')
plt.xticks(range(cancer.data.shape[1]), cancer.feature_names, rotation=90)
plt.hlines(0, 0, cancer.data.shape[1])
plt.ylim(-5, 5)
plt.xlabel('Coefficient index')
plt.ylabel('Coefficient magnitude')
plt.legend()

# coefficients learnt by logistic regression with L1 penalty
for C, marker in zip([0.01, 1, 100], ['o', '^', 'v']):
    lr_l1 = LogisticRegression(C=C, penalty='l1').fit(x_train, y_train)
    print('Training accuracy of l1 logreg with C={:.3f}: {:.2f}'.format(C, lr_l1.score(x_train, y_train)))
    print('Test accuracy of l1 logreg with C={:.3f}: {:.2f}'.format(C, lr_l1.score(x_test, y_test)))
    plt.plot(lr_l1.coef_.T, marker, label='C={:.3f}'.format(C))

plt.xticks(range(cancer.data.shape[1]), cancer.feature_names, rotation=90)
plt.hlines(0, 0, cancer.data.shape[1])
plt.xlabel('Coefficient index')
plt.ylabel('Coefficient magnitude')
plt.ylim(-5, 5)
plt.legend(loc=3)
plt.show()

"""
Linear models for multiclass classification
"""
x, y = make_blobs(random_state=42)
mglearn.discrete_scatter(x[:, 0], x[:, 1], y)
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')
plt.legend(['Class 0', 'Class 1', 'Class 2'])

linear_svm = LinearSVC().fit(x, y)
print('Coefficient shape: ', linear_svm.coef_.shape)
print('Intercept shape: ', linear_svm.intercept_.shape)

# decision boundaries learned by the three one-vs.-rest classifiers
mglearn.discrete_scatter(x[:, 0], x[:, 1], y)
line = np.linspace(-15, 15)
for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_, ['b', 'r', 'g']):
    plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)
plt.ylim(-10, 15)
plt.xlim(-10, 8)
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')
plt.legend(['Class 0', 'Class 1', 'Class 2', 'Line class 0', 'Line class 1', 'Line class 2'], loc=(1.01, 0.3))

# multiclass decison boundaries derived from the three one-vs.-rest classifiers
mglearn.plots.plot_2d_classification(linear_svm, x, fill=True, alpha=.7)
mglearn.discrete_scatter(x[:, 0], x[:, 1], y)
line = np.linspace(-15, 15)
for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_, ['b', 'r', 'g']):
    plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')
plt.legend(['Class 0', 'Class 1', 'Class 2', 'Line class 0', 'Line class 1', 'Line class 2'], loc=(1.01, 0.3))
plt.show()
