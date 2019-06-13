import numpy as np
import re
import pprint

top_k=2
number_of_documents = int(input("How many documents?"))
list_of_documents = []
documents_with_contents = {}
discrete_words = []
print('Enter the documents\' full names (including extension)\n')
for i in range(number_of_documents):
    list_of_documents.append(input())

for i in range(number_of_documents):
    try:
        with open(list_of_documents[i], 'r') as currentDocument:

            document_contents = currentDocument.readlines()
            document_contents = re.findall('\w+', ' '.join(document_contents))
            #TODO find a more efficient way to .lower() the document_contents
            for index in range(len(document_contents)):
                document_contents[index] = document_contents[index].lower()
            for word in document_contents:
                word = word.lower()
                if word in discrete_words:
                    continue
                else:
                    discrete_words.append(word)

            documents_with_contents.update({list_of_documents[i]: document_contents})
    except FileNotFoundError:
        print(f'Document \"{list_of_documents[i]}\" not found.')


#TODO DONE convert string to list cause count doesnt work
d1 = []
document_counted_words = {}
print(f'All documents combined (discrete_words): {discrete_words}')


for document in documents_with_contents:
    for word in discrete_words:
        d1.append(documents_with_contents[document].count(word))
        #d2.append(documents_with_contents['doc4.txt'].count(word))
    document_counted_words.update({document: d1})
    d1 = []
print(document_counted_words)
#use pprint.pprint(documents_with_contents['doc3.txt'])

for doc in list_of_documents:
    print(f'Occurrences of doc1: {document_counted_words[doc]}')
   # print(f'Occurrences of doc2: {d2}')


def cosine_similarity(doc1, doc2):
    dot_product = np.dot(doc1, doc2)
    normalized_d1 = np.linalg.norm(doc1)
    normalized_d2 = np.linalg.norm(doc2)
    cos = dot_product / (normalized_d1 * normalized_d2)
    return cos

#TODO print the TOP-K most similar
#TODO problem is that we cant really sort it
similarities_list = []
for i in range(len(documents_with_contents)):
    for j in range(i+1, len(documents_with_contents)):
        similarities_list.append(f'Similarity of ({list_of_documents[i]}, {list_of_documents[j]}): {cosine_similarity(document_counted_words[list_of_documents[i]], document_counted_words[list_of_documents[j]])}')
print(similarities_list)
print(f'documents_with_contents:{documents_with_contents}')
print(f'list_of_documents:{list_of_documents}')
#print(f'document_index:{document_index}')







'''for i in range(number_of_documents):
    try:
        with open(list_of_documents[i], 'r') as currentDocument:
            document_index[list_of_documents[i]] = i
            discrete_words = {}

            for line in currentDocument:
                line = ' '.join(re.findall('\w+', line))
                for word in line.split():
                    word = word.lower()
                    if word in discrete_words:
                        word_counter = discrete_words[word]
                        word_counter = word_counter+1
                        discrete_words.update({word: word_counter})
                        del word_counter
                    else:
                        discrete_words.update({word: i})
            documents_with_contents.update({list_of_documents[i]: discrete_words})
            del discrete_words'''