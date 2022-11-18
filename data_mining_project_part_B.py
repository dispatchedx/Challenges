import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection
from sklearn import metrics
from keras import Sequential
from keras.layers import Dense, Flatten, Embedding, GlobalMaxPool1D, Dropout, GlobalAveragePooling1D
from keras.callbacks import EarlyStopping

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

nltk.download('punkt')  # needed for nltk
nltk.download('stopwords')  # needed for stopwords removal

# Read csv into a pandas dataframe
data = pd.read_csv('C:/Users/DX/Desktop/work/datamining/onion-or-not.csv')


def preprocessing(dataframe):
    """

    :param dataframe: dataframe with 'text' column that has multiple sentences
    :return: tf_idf vectorized matrix
    """

    def pd_to_list(dataframe):
        """ Append all titles to list and make them lower case """
        document_contents = []
        for index in range(len(dataframe['text'])):
            document_contents.append(dataframe['text'][index].lower())
        return document_contents

    def depunctuate(list_of_strings):
        """ Remove punctuations (except ‘) """
        depunctuated_list = [re.sub('[!@#$%&’()*+,\\\'-./:;”“<=>?\"[\]^_—`{|}~\d…]', '', title) for title in
                             list_of_strings]
        return depunctuated_list

    def discretize(list_of_strings):
        """ Remove repeating words from each title
        :param list_of_strings:
        :return: list of strings
         """
        discrete_titles = [list(set(title.split())) for title in list_of_strings]
        return discrete_titles

    def stemming(list_of_strings):
        """
        Stems words from the titles
        :param list_of_strings: list of titles
        :return: list of titles
        """
        stemmer = nltk.stem.PorterStemmer()
        stemmed_titles = []
        for title in list_of_strings:
            temp = []
            for word in title:
                temp.append(stemmer.stem(word))
            stemmed_titles.append(temp)
        return stemmed_titles

    def stop_words_removal(list_of_strings):
        """
        Removes stop words from the titles
        :param list_of_strings: list of titles
        :return: list of titles
        """
        stop_words = set(nltk.corpus.stopwords.words('english'))
        sp_titles = []
        for title in list_of_strings:
            temp = []
            for word in title:
                if word not in stop_words:
                    temp.append(word)
            sp_titles.append(temp)
        # Convert back to list of strings
        list_of_strings = [' '.join(title) for title in sp_titles]
        return list_of_strings

    def tf_idf(list_of_strings):
        """
        applies tf_idf on list of strings
        :param list_of_strings:
        :return: tf_idf vectorized matrix
        """
        tf_counter = TfidfVectorizer()
        X = tf_counter.fit_transform(list_of_strings)
        return X

    titles = pd_to_list(dataframe)
    titles = depunctuate(titles)
    titles = discretize(titles)
    titles = stemming(titles)
    titles = stop_words_removal(titles)
    #X = tf_idf(titles) # tf_idf ruins it idk why
    # will just vectorize instead for now..

    tokenizer = Tokenizer(8000, split=' ')
    tokenizer.fit_on_texts(titles)

    X = tokenizer.texts_to_sequences(titles)
    X = pad_sequences(X)
    return X


X = preprocessing(data)
target = data['label'].values
# Splitting training-testing data to 75%-25%
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, target, test_size=0.25, random_state=1)

model = Sequential()
model.add(Embedding(8000, 128, input_length = X.shape[1]))  # better instead of flatten for words though we have tf_idf

#model.add(Dense(128, activation='relu')) # doesnt do anything
#model.add(Flatten()) #trash and slow

model.add(Dense(128, activation='relu'))
model.add(GlobalAveragePooling1D()) # pretty good
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# cross entropy loss function is for a binary classification
# adam because its an efficient stochastic gradient descent algorithm because it automatically tunes itself and gives good results in a wide range of problems
model.summary()
# Callback to stop training when val_loss stops getting reduced (to not overfit)
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1)

history = model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test), callbacks=[es])
predictions = model.predict(X_test)
y_predict = [round(x[0]) for x in predictions]  # prediction is 1 if probability > 50% and 0 if its < 50%
print(metrics.classification_report(y_predict, y_test))

