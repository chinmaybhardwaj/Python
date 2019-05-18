# -*- coding: utf-8 -*-

from sklearn.feature_extraction import DictVectorizer
import numpy as np

# 
# Using DictVectorizer for creating extra columns for categories
#

# Sample Data
data = [
        {'price': 850000, 'rooms': 5, 'neighborhood': 'Queen Anne'},
        {'price': 700000, 'rooms': 4, 'neighborhood': 'Fremont'},
        {'price': 650000, 'rooms': 3, 'neighborhood': 'Wallingford'},
        {'price': 600000, 'rooms': 3, 'neighborhood': 'Fremont'},
        {'price': 550000, 'rooms': 2, 'neighborhood': 'Queen Anne'},
        {'price': 500000, 'rooms': 1, 'neighborhood': 'Fremont'},
    ]

print('\nData: \n', data)

# Using 'One-Hot Encoding'. Creates extra columns indication presence/absence of categoryy
vec = DictVectorizer(sparse=False, dtype=np.int16)
X = vec.fit_transform(data)

# vector containing 3 extra columns
print('\nVectorized Data: \n', X)
# Get column names
print('\nVectorized Column names: \n', vec.get_feature_names())