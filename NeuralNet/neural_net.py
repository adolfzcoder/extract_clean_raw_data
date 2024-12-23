from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd
import matplotlib as plt


results_data = pd.read_csv('output_gr11_FT_6.csv')
results_data
X = results_data.drop(columns = ['points'])
y = results_data['points']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = DecisionTreeClassifier()
model.fit(X_train, y_train)
#model.fit(X, y)
#predictions = model.predict( [[1708,46,0,6]] )
predictions = model.predict(X_test)
predictions
score = accuracy_score(y_test, predictions)
score