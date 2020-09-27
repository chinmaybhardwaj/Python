# -*- coding: utf-8 -*-

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix

data = fetch_20newsgroups()

print(data.target_names)
categories = ['talk.religion.misc', 'soc.religion.christian', 'sci.space', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

print(train.data[5])
#Create pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
# Train model
model.fit(train.data, train.target)
# make prediction
prediction = model.predict(test.data)

mat = confusion_matrix(test.target, prediction)
print('\nConfusion Matrix: \n',mat)

def predict_category(s, train=train, model=model):
    pred = model.predict([s])
    return train.target_names[pred[0]]


print('\n\nPredict 1:', predict_category('sending a payload to ISS'))
print('Predict 2:', predict_category('discussing islam and atheism'))
print('Predict 3:', predict_category('determining the screen resolution'))