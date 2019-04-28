#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Introduction to Machine Learning with Python
Chapter 2
Supervised Learning - Ensembles of Decision Trees
"""

import matplotlib.pyplot as plt
import numpy as np
import mglearn
from sklearn import datasets
from sklearn import ensemble
from sklearn import model_selection

"""
Analyzing random forests
"""


def plot_feature_importances_cancer(model):
    n_features = cancer.data.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), cancer.feature_names)
    plt.xlabel('Feature importance')
    plt.ylabel('Feature')
    plt.show()


x, y = datasets.make_moons(n_samples=100, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, stratify=y, random_state=42)

forest = ensemble.RandomForestClassifier(n_estimators=5, random_state=2)
forest.fit(x_train, y_train)

fig, axes = plt.subplots(2, 3, figsize=(20, 20))
for i, (ax, tree) in enumerate(zip(axes.ravel(), forest.estimators_)):
    ax.set_title('Tree {}'.format(i))
    mglearn.plots.plot_tree_partition(x_train, y_train, tree, ax=ax)

mglearn.plots.plot_2d_separator(forest, x_train, fill=True, ax=axes[-1, -1], alpha=.4)
axes[-1, -1].set_title('Random Forest')
mglearn.discrete_scatter(x_train[:, 0], x_train[:, 1], y_train)

# apply a random forest consisting of 100 trees
cancer = datasets.load_breast_cancer()
x_train100, x_test100, y_train100, y_test100 = model_selection.train_test_split(cancer.data, cancer.target,
                                                                                random_state=0)
forest100 = ensemble.RandomForestClassifier(n_estimators=100, random_state=0)
forest100.fit(x_train100, y_train100)

print('Accuracy on training set: {:.3f}'.format(forest100.score(x_train100, y_train100)))
print('Accuracy on test set: {:.3f}'.format(forest100.score(x_test100, y_test100)))

plot_feature_importances_cancer(forest100)
