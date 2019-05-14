import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# =============================================================================
# Predict Breast Cancer as  benign or malignant using KNN
# Dataset: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29
# =============================================================================

df = pd.read_csv('./dataset/breast-cancer-wisconsin.data.txt')
# Replace missing value with -99999
df.replace('?',-99999, inplace=True)
# Drop unwanted column
df.drop(['id'], 1, inplace=True)
print(df.head())
print(df.keys())

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

# Split data into test and train
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2)
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(train_X, train_y)

# Predict on test data
prediction = clf.predict(test_X)
print('Prediction of test data: ', prediction)

# Get classifier accuracy
accuracy = clf.score(test_X, test_y)
print('Accuracy: ', accuracy)



# Sample data
example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures), -1)
# Predict sample data
prediction = clf.predict(example_measures)
print('Prediction: ', prediction) # (2 for benign, 4 for malignant)