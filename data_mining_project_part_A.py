import pandas as pd
from sklearn import linear_model
from sklearn import model_selection
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.cluster import KMeans

# reading csv data
data = pd.read_csv('C:/Users/DX/Desktop/datamining/winequality-red.csv')
print(data.columns)

# labels
X = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
          'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']].values
# target
y = data['quality'].values
def average_ph(X):
    # Calculating average pH value
    sum = 0
    for i in range(0, len(X)):
        sum += X[i][-3] # -3 is pH column
    average = sum/len(X)
    print(average)

# Splitting training-testing data at 75%-25%
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25, random_state=1)

Xx = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
           'total sulfur dioxide', 'density', 'sulphates', 'alcohol', 'quality']].values
# target
yy = data['pH'].values

# Splitting training data again to have 33% of pH values set to None
Xx_train, Xx_test, yy_train, yy_test = model_selection.train_test_split(Xx, yy, test_size=0.33, random_state=1)
for i in range(len(yy_test)):
    yy_test[i] = None

# fit regression model
regress = linear_model.LinearRegression()
regress.fit(Xx_train, yy_train)
yy_predict = regress.predict(Xx_test)

''' 4.
kmeans = KMeans(n_clusters=6).fit(Xx)
cluster_map = pd.DataFrame()
cluster_map['data_index'] = data.index.values
cluster_map['cluster'] = kmeans.labels_
print(cluster_map)
plt.scatter(data['quality'], data['pH'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.show()
'''


# Replacing all None pH values with regression predictions

for i in range(0, len(yy_test)):
    yy_test[i] = yy_predict[i]


''' 2.
# Replacing all None pH values with the average pH value
for i in range(0, len(X), 3):
    X[i][-3] = average_pH
'''
print("What to do?\n"
      "1. Remove pH column\n"
      "2. Fill missing values with average pH\n"
      "3. Fill missing values with Logistic Regression\n"
      "4. Fill missing values with K-means cluster average\n")

# fit SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_predict = svclassifier.predict(X_test)


df = pd.DataFrame({'Real': yy_test.flatten(), 'Prediction': yy_predict.flatten()})
print(df.head(10))


# Print metrics report
print(metrics.classification_report(y_test, y_predict))
