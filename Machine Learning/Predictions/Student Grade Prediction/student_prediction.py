import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm

# =============================================================================
#  Read Student dataset from the 'student/student-mat.csv'
#  Check description of each feature from 'student/student.txt'
# =============================================================================

df = pd.read_csv('./student/student-mat.csv', delimiter=';')

print(df.head())

# Features:
#['school' 'sex' 'age' 'address' 'famsize' 'Pstatus' 'Medu' 'Fedu' 'Mjob'
#'Fjob' 'reason' 'guardian' 'traveltime' 'studytime' 'failures'
# 'schoolsup' 'famsup' 'paid' 'activities' 'nursery' 'higher' 'internet'
# 'romantic' 'famrel' 'freetime' 'goout' 'Dalc' 'Walc' 'health' 'absences'
# 'G1' 'G2' 'G3']

student_dataset = df[['age','studytime', 'G1', 'G2', 'G3']]
train_X, test_X, train_y, test_y = train_test_split(student_dataset,
                                                    student_dataset['G3'],
                                                    random_state=0)

clf = svm.SVC(kernel='linear')

# Train classifier
clf.fit(train_X, train_y)

# Predict test dataset
prediction = clf.predict(test_X)
print('Predictions: ', prediction)
# Check Score
score = clf.score(test_X, test_y)
print('Score: ', score)
