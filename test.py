import pandas as pd
from sklearn import datasets, linear_model
from numpy.random import RandomState
from matplotlib import pyplot as plt
from sklearn import model_selection
from sklearn import metrics

data = pd.read_csv('C:/Users/DX/Desktop/datamining/winequality-red.csv')
print(data.columns)
rng = RandomState()
#print(data.isnull().any()) if false no null values in column
X = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
          'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']].values
y = data['quality'].values
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25, random_state=1)


# fit a model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)

print(model.intercept_)
#print(model.coef_)
y_predict = model.predict(X_test)

df = pd.DataFrame({'Real': y_test.flatten(), 'Prediction': y_predict.flatten()})
print(df.head(10))
#print(f'Score:, {metrics.recall_score(y_test, y_predict)}')
