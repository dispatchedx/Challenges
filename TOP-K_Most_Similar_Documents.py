import numpy as np
import re


def cosine_similarity(doc1, doc2):
    dot_product = np.dot(doc1, doc2)
    normalized_doc1 = np.linalg.norm(doc1)
    normalized_doc2 = np.linalg.norm(doc2)
    cos = dot_product / (normalized_doc1 * normalized_doc2)
    return cos


number_of_documents = int(input("How many documents?"))
documents_with_contents = {}
discrete_words = []
list_of_documents = []
print('Enter the documents\' full names (ex. doc.txt)\n')
for i in range(number_of_documents):
    list_of_documents.append(input())

for i in range(number_of_documents):
    try:
        with open(list_of_documents[i], 'r') as currentDocument:
            document_contents = currentDocument.readlines()
            document_contents = re.findall('\w+', ' '.join(document_contents))

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
        print(f'File \"{list_of_documents[i]}\" was not found; files must be placed in the same folder as the program')

vectorized = []
vectorized_documents = {}
for document in documents_with_contents:
    for word in discrete_words:
        vectorized.append(documents_with_contents[document].count(word))
    vectorized_documents.update({document: vectorized})
    vectorized = []

similarities_dict = {}
for i in range(len(documents_with_contents)):
    for j in range(i+1, len(documents_with_contents)):
        cosine_result = cosine_similarity(vectorized_documents[list_of_documents[i]],
                                          vectorized_documents[list_of_documents[j]])
        similarities_dict.update({f'({list_of_documents[i]}, {list_of_documents[j]})': cosine_result})
similarities_sorted = sorted(similarities_dict, key=similarities_dict.get, reverse=True)

top_k = int(input("Enter a number K to print the top_K most similar documents"))
for i, r in enumerate(similarities_sorted):
    if i < top_k:
        print(f'{i+1}.{r}: {similarities_dict[r]}')
