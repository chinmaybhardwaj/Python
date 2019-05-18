# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

#
# Shows 2 methods for converting text features into dataframe
#

# Sample Data
sample = [
            'problem of evil',
            'evil queen',
            'horizon problem'
        ]
print('Sample Data:\n', sample)


# Method 1 : Enconding data based on word count
vec = CountVectorizer()
X = vec.fit_transform(sample)
# Convert vect to pandas df
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
print('\nDataFrame:\n', df)



# Method 2: Using Term Frequency-Inverse Document Frequency(TF-IDF)
vec2 = TfidfVectorizer()
X2 = vec2.fit_transform(sample)
# Convert vect to pandas df
df2 = pd.DataFrame(X2.toarray(), columns=vec2.get_feature_names())
print('\nDataFrame using TF-IDF:\n', df2)