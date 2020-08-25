import pandas as pd
from sklearn import linear_model
from sklearn import model_selection
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.cluster import KMeans
import numpy as np

# reading csv data
data = pd.read_csv('C:/Users/DX/Desktop/work/datamining/winequality-red.csv')

# labels
X = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
          'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']].values
# target
y = data['quality'].values


def average_ph(X):
    """

    :param X: data
    :return: average of pH column
    """
    sum = 0
    for i in range(0, len(X)):
        sum += X[i][-3] # -3 is pH column
    average = sum/len(X)
    return average


def train_svc_model(X, y):
    """
    Splits training-testing data to 75%-25%, trains a SVC model and prints its metrics
    :param X: features
    :param y: target variable
    """
    # Splitting training-testing data at 75%-25%
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25, random_state=1)
    # fit SVC
    svclassifier = SVC(kernel='linear')
    print("Training svc model..")
    svclassifier.fit(X_train, y_train)
    # Print metrics report
    y_predict = svclassifier.predict(X_test)
    print("Training finished, results are:\n")
    print(metrics.classification_report(y_test, y_predict))

def remove_33_of_ph_values():
    """

    :return: split data but yy_test is 33% of pH values and set to None
    """
    Xx = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
               'total sulfur dioxide', 'density', 'sulphates', 'alcohol', 'quality']].values
    # target
    yy = data['pH'].values

    # Splitting training data again to have 33% of pH values set to None
    Xx_train, Xx_test, yy_train, yy_test = model_selection.train_test_split(Xx, yy, test_size=0.33, random_state=1)
    for i in range(len(yy_test)):
        yy_test[i] = None

    return Xx_train, Xx_test, yy_train, yy_test


print("What to do?\n"
      "1. Part A (split dataset to training-test 75%-25% and predict quality)\n"
      "2. Part B (remove 33% of ph values and fill them with various ways)\n"
      "Any other key. Quit\n")

choice = input()
if choice == '1':
    train_svc_model(X, y)
    exit(1)
elif choice == '2':


    print("What to do?\n"
          "1. Remove pH column\n"
          "2. Fill missing values with average pH\n"
          "3. Fill missing values with Logistic Regression\n"
          "4. Fill missing values with K-means cluster average\n"
          "Any other key. Quit\n")
    choice = input()
    if choice == '1':
        X = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                  'free sulfur dioxide', 'total sulfur dioxide', 'density', 'sulphates', 'alcohol']].values
        print("pH column removed")
        train_svc_model(X, y)
    elif choice == '2':
        average = average_ph(X)
        for i in range(0, len(X), 3):
            X[i][-3] = average
        print(f"33% of pH column replaced with average pH={average}")
        train_svc_model(X, y)

    elif choice == '3':
        Xx_train, Xx_test, yy_train, yy_test = remove_33_of_ph_values()
        # fit regression model
        regress = linear_model.LinearRegression()
        print("Training regression model..")
        regress.fit(Xx_train, yy_train)
        print("Regression model finished training")
        yy_predict = regress.predict(Xx_test)
        # replace none values with predictions
        for i in range(0, len(yy_test)):
            yy_test[i] = int(yy_predict[i])
        X = data[
            ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
             'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']].values
        yy = np.concatenate([yy_train,yy_test])
        for i in range(len(X)):
            X[i][-3] = yy[i]
        y = data['quality'].values
        train_svc_model(X, y)
    elif choice == '4':
        # Removing 33% of pH values
        Xx_train, yy_train, Xx_test, yy_test = remove_33_of_ph_values()
        kmeans = KMeans(n_clusters=6).fit(X)
        labels = kmeans.predict(X)
        centroids = kmeans.cluster_centers_
        cluster_map = pd.DataFrame()
        cluster_map['data_index'] = data.index.values
        cluster_map['cluster'] = kmeans.labels_
        print(cluster_map)
        train_svc_model(X, y)
        #plt.scatter(data['quality'], data['pH'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
        #plt.show()
    else:
        exit(1)
else:
    exit(1)
