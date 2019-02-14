# -*- coding: utf-8 -*-

from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB
import numpy as np
import matplotlib.pyplot as plt

X,y = make_blobs(100, centers=2, random_state=2, cluster_std=1.5)
plt.plot(X[:,0], X[:, 1])

model = GaussianNB()
model.fit(X,y)

# Generate new random data
rng = np.random.RandomState(0)
Xnew = [-6, -14] + [14, 18] * rng.rand(2000,2)
ynew = model.predict(Xnew)
print('Prediction: ', ynew)
