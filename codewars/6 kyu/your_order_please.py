def order(sentence):
    if sentence == '':
        return ''
    else:
        dict_of_words = {}
        word = ''
        word_index = 0
        for c in sentence:
            word += c
            if c.isdigit():
                word_index = c
            elif c == ' ':
                dict_of_words[word_index] = word[:len(word)-1]
                word = ''
        else:
            dict_of_words[word_index] = word
    sentence = ''
    for s_key in range(1, len(dict_of_words)+1):
        sentence += dict_of_words.get(str(s_key)) + ' '
    return sentence[:len(sentence)-1]


#    genius: def order(sentence):
#    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
