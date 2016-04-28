string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
wordList = string.split()
wordLenList = list()
for word in wordList:
	word.replace(".", "")
	word.replace(",", "")
	wordLenList.append(len(word))
print (wordLenList)
