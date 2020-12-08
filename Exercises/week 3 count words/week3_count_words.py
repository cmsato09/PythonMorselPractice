import string

def count_words(words):

    word_list = words.split()  # make list of words from given variable
    for i, wd in enumerate(word_list):
        if wd[-1] in string.punctuation:
            word_list[i] = word_list[i].strip(string.punctuation)

    word_count = {}  # empty dictionary to store word and count
    for w in word_list:
        if w.lower() in word_count:
            continue
        else:
            word_count.update({w.lower(): word_list.count(w)})
    return word_count

