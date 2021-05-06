import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/heart.csv')
df['output'] = df['output'] - 1

predictors = ['chestpain', 'exercise']
X = df[predictors].values
y = df['output'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

blind_prediction = np.median(y_train) #median? i thought blind was mean?
print((y_test == blind_prediction).mean())

clf = CategoricalNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
y_prob = clf.predict_proba(X_test) # why do we want probability/what probability

clf.score(X_test, y_test)

df.describe()
