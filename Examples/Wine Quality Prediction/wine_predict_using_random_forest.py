'''
    This script shows predictions of wine using RandomForestClassifier 
'''

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load data from Datasets
wine_dataset = datasets.load_wine()


# Check all keys
print('Keys: {}'.format(wine_dataset.keys()))

# Wine Names
print('Target Name: {}'.format(wine_dataset['target_names']))

# Feature Names
print('Feature Name: {}'.format(wine_dataset['feature_names']))

# Type of data
print('Type of data: {}'.format(type(wine_dataset['data'])))

# Shape of Data
print('Shape of Data: {}'.format(wine_dataset['data'].shape))

# View Data
print('View Data: {}'.format(wine_dataset['data'][:5]))

train_X, test_X, train_y, test_y = train_test_split(wine_dataset['data'],
                                                    wine_dataset['target'],
                                                    random_state=0)

# Create model
clf = RandomForestClassifier(n_estimators=10)

# Train model
clf.fit(train_X, train_y)

# Predict data
predictions = clf.predict(test_X)
print('Predictions: ', predictions)

# Check Score
score = clf.score(test_X, test_y)
print('Score: ', score)