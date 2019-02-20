# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score



# =============================================================================
#  Read Titanic dataset from the 'dataset/test.csv',  'dataset/train.csv'
#  Final test results are stored in 'dataset/titanic_submission.csv'
# =============================================================================

train_df = pd.read_csv('./dataset/train.csv')
test_df = pd.read_csv('./dataset/test.csv')

print(train_df.head())
print(train_df.keys())
print(train_df.isnull().sum())


sns.countplot('Survived', data=train_df)
plt.show()

survived_mean = train_df['Survived'].mean()
print('Mean:', survived_mean)

survived_groupby_mean = train_df.groupby(['Sex', 'Pclass']).mean()
print('Group By Mean:', survived_groupby_mean)
survived_groupby_mean['Survived'].plot(kind='bar')

print('Age: \n', train_df['Age'].describe())

# Train dataset
dummies_sex = pd.get_dummies(train_df['Sex'],prefix='Sex')
train_df = pd.concat([train_df,dummies_sex],axis=1)
dummies_class = pd.get_dummies(train_df['Pclass'],prefix='Pclass')
train_df = pd.concat([train_df,dummies_class],axis=1)
print(train_df.keys())

# Test dataset
test_sex = pd.get_dummies(test_df['Sex'],prefix='Sex')
test_df = pd.concat([test_df,test_sex],axis=1)
test_class = pd.get_dummies(test_df['Pclass'],prefix='Pclass')
test_df = pd.concat([test_df,test_class],axis=1)
print(test_df.keys())


# Creating model
lr = LogisticRegression()

columns = ['Pclass_2', 'Pclass_3', 'Sex_male']

all_X = train_df[columns]
all_y = train_df['Survived']

train_X, test_X, train_y, test_y = train_test_split(
    all_X, all_y, test_size=0.2,random_state=0)

lr.fit(train_X, train_y)
prediction = lr.predict(test_X)
accuracy = accuracy_score(test_y, prediction)

print('Accuracy:', accuracy)


# Create confusion matrix
conf_matrix = confusion_matrix(test_y, prediction)
conf_df = pd.DataFrame(conf_matrix, columns=['Survived', 'Died'], index=[['Survived', 'Died']])
print('Confusion Matrix: \n', conf_df)

# Use Cross Validation
scores = cross_val_score(lr, all_X, all_y, cv=10)
mean_score = np.mean(scores)
print('Mean Score: ', mean_score)

# Predict Test data
lr.fit(all_X, all_y)
test_prediction = lr.predict(test_df[columns])
print('Test data prediction: ', test_prediction)


holdout_ids = test_df["PassengerId"]
submission_df = {"PassengerId": holdout_ids,
                 "Survived": test_prediction}
submission = pd.DataFrame(submission_df)
submission.to_csv('titanic_submission.csv', index=False)