from nltk import stem

stemming = stem.PorterStemmer()
for word in open("knock51_output.txt", "r"):
    word = word.strip("\n")
    print ("{}\t{}".format(word, stemming.stem(word)))
