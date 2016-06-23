# code = utf-8
import sys
from nltk.corpus import stopwords

my_stop_word  = stopwords.words('english')
my_stop_word += ["[","]","'s", "``", "…", "—", "–", "-","--", "-–", "/", "'","''", "(", ")", ";", "*", ".", "!", ",", ":", "#", "$", "%", "&"]

def is_stop_word(word):
	if word in my_stop_word or word in stopwords.words('english'):
		return True
	else:
		return False
# http://dev.mysql.com/doc/refman/5.6/ja/fulltext-stopwords.html
# , "'d","n't"

stop_word2=list()
for item in sys.argv[1:]:
	if item in stop_word:
		stop_word2.append(item)

print(" ".join(sorted(stop_word2)))