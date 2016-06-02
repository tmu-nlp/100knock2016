from knock51 import getWords
from nltk.stem.lancaster import LancasterStemmer


st = LancasterStemmer()
words = getWords()
for word in words:
    print(st.stem(word.strip().strip(",").strip(".")))
