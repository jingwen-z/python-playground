#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Introduction to Machine Learning with Python
Chapter 2
Supervised Learning - Decision Trees
"""

import graphviz
import mglearn.datasets
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

mglearn.plots.plot_animal_tree()

"""
Controlling complexity of decision trees
"""
cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)

# tree = DecisionTreeClassifier(random_state=0)
# tree.fit(x_train, y_train)
# print('Accuracy on training set: {:.3f}'.format(tree.score(x_train, y_train)))
# print('Accuracy on test set: {:.3f}'.format(tree.score(x_test, y_test)))

tree = DecisionTreeClassifier(max_depth=4, random_state=0)
tree.fit(x_train, y_train)
print('Accuracy on training set: {:.3f}'.format(tree.score(x_train, y_train)))
print('Accuracy on test set: {:.3f}'.format(tree.score(x_test, y_test)))

"""
Analyzing decision trees
"""
export_graphviz(tree, out_file='tree.dot', class_names=['malignant', 'benign'],
                feature_names=cancer.feature_names, impurity=False, filled=True)

with open('tree.dot') as f:
    dot_graph = f.read()

graphviz.Source(dot_graph).view()
