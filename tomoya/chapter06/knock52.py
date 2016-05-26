from knock50 import getSentence
from knock51 import getWords
from  stemming.porter2 import stem

words = getWords()
for word in words:
  print(stem(word.strip().strip(",").strip(".")))
