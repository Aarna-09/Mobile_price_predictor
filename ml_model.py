import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
import pickle

dataset = pd.read_csv('Mobile Price Prediction Datatset.csv')


dataset.dropna(inplace=True)

dataset.drop(columns=['Unnamed: 0', 'Brand me'], inplace=True)

X = dataset.drop(columns='Price')
y = dataset['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = DecisionTreeRegressor(random_state=0)
model.fit(X_train, y_train)

pickle.dump(model, open('model_saved (2)' , 'wb'))
