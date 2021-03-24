# literaly exists cause i need a bio.txt to be less than 100 words

sentences = []
with open("bio.txt") as bio:
    for word in bio:
        sentences.append(word.split())
    words = []
    for j in range(len(sentences)):
        words = words+sentences[j]
    print(len(words))
    print(words)


