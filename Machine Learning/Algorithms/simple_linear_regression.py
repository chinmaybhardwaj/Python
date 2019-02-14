# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
#
# Simple linear regression i.e. fitting the line to (x,y) data
#

rng = np.random.RandomState(42)

# Get random x,y values
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)


X = x[:, np.newaxis]
print("X shape:", X.shape)

# Initialize model
model = LinearRegression(fit_intercept=True)

model.fit(X,y)

# Create Test data
xfit = np.linspace(-1,11)
Xfit = xfit[:,np.newaxis]
yfit = model.predict(Xfit)

# Plot x,y data 
plt.scatter(x,y)
plt.plot(xfit,yfit)