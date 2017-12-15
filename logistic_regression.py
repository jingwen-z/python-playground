# -*- coding: utf-8 -*-
"""
Python Machine Learning Cookbook
Chapter 2
Building a logistic regression classifier
"""

import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


def plot_classifier(X):
    x_min, x_max = min(X[:, 0]) - 1.0, max(X[:, 0]) + 1.0
    y_min, y_max = min(X[:, 1]) - 1.0, max(X[:, 1]) + 1.0
    return x_min, x_max, y_min, y_max


X = np.array([[4.0, 7.0], [3.5, 8.0], [3.1, 6.2], [0.5, 1.0], [1.0, 2.0],
              [1.2, 1.9], [6.0, 2.0], [5.7, 1.5], [5.4, 2.2]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])

classifier = linear_model.LogisticRegression(solver='liblinear', C=100)
classifier.fit(X, y)

x_min = plot_classifier(X)[0]
x_max = plot_classifier(X)[1]
y_min = plot_classifier(X)[2]
y_max = plot_classifier(X)[3]

# denotes the step size that will be used in the mesh grid
step_size = 0.01

# define the mesh grid
x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))

# compute the classifier output
mesh_output = classifier.predict(np.c_[x_values.ravel(), y_values.ravel()])

# reshape the array
mesh_output = mesh_output.reshape(x_values.shape)

# Plot the output using a colored plot
plt.figure()

# choose a color scheme
plt.pcolormesh(x_values, y_values, mesh_output, cmap=plt.cm.gray)

plt.scatter(X[:, 0], X[:, 1], c=y, s=80, edgecolors='black', linewidth=1, cmap=plt.cm.Paired)

# specify the boundaries of the figure
plt.xlim(x_values.min(), x_values.max())
plt.ylim(y_values.min(), y_values.max())

# specify the ticks on the X and Y axes
plt.xticks((np.arange(int(x_min), int(x_max), 1.0)))
plt.yticks((np.arange(int(min(X[:, 1]) - 1), int(max(X[:, 1]) + 1), 1.0)))

plt.show()
