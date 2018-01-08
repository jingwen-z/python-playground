#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Introduction to Machine Learning with Python
Chapter 2
Supervised Learning - Ensembles of Decision Trees
"""

import matplotlib.pyplot as plt
import mglearn
from sklearn import datasets
from sklearn import ensemble
from sklearn import model_selection

"""
Analyzing random forests
"""
x, y = datasets.make_moons(n_samples=100, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, stratify=y, random_state=42)

forest = ensemble.RandomForestClassifier(n_estimators=5, random_state=2)
forest.fit(x_train, y_train)
print('forest:', forest)

fig, axes = plt.subplots(2, 3, figsize=(20, 20))
for i, (ax, tree) in enumerate(zip(axes.ravel(), forest.estimators_)):
    ax.set_title('Tree {}'.format(i))
    mglearn.plots.plot_tree_partition(x_train, y_train, tree, ax=ax)

mglearn.plots.plot_2d_separator(forest, x_train, fill=True, ax=axes[-1, -1], alpha=.4)
axes[-1, -1].set_title('Random Forest')
mglearn.discrete_scatter(x_train[:, 0], x_train[:, 1], y_train)
plt.show()