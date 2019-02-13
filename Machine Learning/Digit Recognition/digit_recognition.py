# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Read dataset from CSV using Pandas
data = pd.read_csv('train.csv')


# Check all keys
print('Keys: {}'.format(data.keys()))

# Show first 5 rows of data
print(data.head())

# Convert data into 2D array 
digit_dataset = data.values

# Create Classifier
clf = DecisionTreeClassifier(digit_dataset[],
                             digit_dataset['label'],
                             random_state=0)

#train_X, test_X, train_y, test_y = train_test_split()



