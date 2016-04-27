# knock09.py
import random
string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
wordList = []
for word in (string.split()):
	if len(word) <= 4:
		wordList.append(word)
	else:
		ls = list(word[1:-1])
		random.shuffle(ls)
		wordList.append(word[0] + "".join(ls) + word[-1])

print(" ".join(wordList))