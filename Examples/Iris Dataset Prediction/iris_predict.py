from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

iris_dataset = load_iris()

# Check all keys
print('Keys: {}'.format(iris_dataset.keys()))

# Flower Names
print('Species Name: {}'.format(iris_dataset['target_names']))

# Feature Names
print('Feature Name: {}'.format(iris_dataset['feature_names']))

# Type of data
print('Type of data: {}'.format(type(iris_dataset['data'])))

# Shape of Data
print('Shape of Data: {}'.format(iris_dataset['data'].shape))

# View Data
print('View Data: {}'.format(iris_dataset['data'][:5]))


# Split data into training and test 
train_X, test_X, train_y, test_y = train_test_split(iris_dataset['data'], 
                                                  iris_dataset['target'],
                                                  random_state=0)

# View the data
iris_dataframe = pd.DataFrame(train_X, columns=iris_dataset['feature_names'])
#
pd.plotting.scatter_matrix(iris_dataframe, c=train_y, figsize=(15,15), marker='o', 
                           hist_kwds={'bins': 20}, s=60) #, aplha=.8, cmap=mglearn.cm3) 

# Implement K-Nearest Neighbors Model
knn = KNeighborsClassifier(n_neighbors=1) # n_neighbor no. of neighbors for training model

# Fit the knn model with training data
knn.fit(train_X, train_y)

# Predict Test data
prediction = knn.predict(test_X)
print('Validation Prediction:', prediction)

# Check Test score
score1 = np.mean(prediction == test_y)
score2 = knn.score(test_X, test_y)

print('Check Score:')
print('Method 1:', score1) # 0.97 = 97%
print('Method 2:', score2) # 0.97 = 97%

