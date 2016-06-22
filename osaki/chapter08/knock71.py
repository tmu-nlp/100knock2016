import sys
from nltk.corpus import stopwords

stopset=stopwords.words("english")

if sys.argv[1] in stopset:
    print("true")
else:
    print("false")
