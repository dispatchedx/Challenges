import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import model_selection
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import sklearn.metrics

nltk.download('punkt') # needed for nltk
nltk.download('stopwords') # needed for stopwords removal
# Read csv into a pandas dataframe
data = pd.read_csv('C:/Users/DX/Desktop/datamining/onion-or-not.csv')

# Convert dataframe to dictionary
titles_dict = data.to_dict('list')
discrete_words = []

document_contents = []

# Append all titles to list and make them lower case
for index in range(len(titles_dict.get('text'))):
    document_contents.append(titles_dict.get('text')[index].lower())

# Remove punctuations (not ‘ ')
#all_words=[]
document_contents = [re.sub('[!@#$%&’()*+,\\\'-./:;”“<=>?\"[\]^_—`{|}~\d…]', '', title) for title in document_contents]
discrete_titles = [list(set(title.split())) for title in document_contents]
'''
for title in document_contents:
    # Place all discrete words in a list
    for word in title.split():
        all_words.append(word)
        if word in discrete_words:
            continue
        else:
            discrete_words.append(word)
'''
#discrete_words = set(all_words)


def stemming(titles):
    """
    Stems words from the titles
    :param titles: list of titles
    :return: list of titles
    """
    stemmer = nltk.stem.PorterStemmer()
    stemmed_titles = []
    for title in titles:
        temp = []
        for word in title:
            temp.append(stemmer.stem(word))
        stemmed_titles.append(temp)
    return stemmed_titles


def stop_words_removal(titles):
    """
    Removes stop words from the titles
    :param titles: list of titles
    :return: list of titles
    """
    stop_words = set(nltk.corpus.stopwords.words('english'))
    sp_titles = []
    for title in titles:
        temp = []
        for word in title:
            if word not in stop_words:
                temp.append(word)
        sp_titles.append(temp)
    return sp_titles


# Stopwords removal
discrete_titles = stemming(discrete_titles)
# Stemming
discrete_titles = stop_words_removal(discrete_titles)

discrete_titles = [' '.join(title) for title in discrete_titles]
final_data = pd.DataFrame({'titles': discrete_titles, 'label': data['label'].values})

counter = CountVectorizer()
tf_counter = TfidfVectorizer()
X = tf_counter.fit_transform(discrete_titles)

print(tf_counter.get_feature_names())
x_train = X[:18000]
x_test = X[18000:]

labels = list(final_data['label'].values)
y_train = labels[:18000]
y_test = labels[18000:]

#x_train = counter.fit_transform(x_train)
#x_test = counter.transform(x_test)

#y_pred = classifier.predict(x_test)
print('jee')
#print(sklearn.metrics.classification_report(y_test, y_pred))
#print('xtrain', x_train.shape)
print('tfidf', x_train.shape)
print('ytrain' ,np.asarray(y_train).T.shape)
print(final_data['label'].values.shape)


class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(17729, 5000)  # 17729 rows
        self.weights2 = np.random.rand(5000, 5000)
        self.y = y
        self.output = np.zeros(np.asarray(self.y).shape)

    def forward_propagation(self):
        self.layer1 = self.sigmoid(np.dot(self.input, self.weights1))
        self.output = self.sigmoid(np.dot(self.layer1, self.weights2))

    def back_propagation(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * self.sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * self.sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)


NN = NeuralNetwork(x_train, y_train)

for i in range(5):
    NN.forward_propagation()
    NN.back_propagation()

print('je')
print(NN.output)
