from collections import defaultdict
string = "I am an NLPer"
wordBiGram = defaultdict(lambda: 0)
letterBiGram = defaultdict(lambda: 0)

def trainFromStr(str_in):
	wordList = string.split()
	for i in range(len(wordList) - 1):
		wordBiGram[wordList[i] + " " + wordList[i+1]] += 1

	for i in range(len(str_in) - 1):
		letterBiGram[str_in[i:i + 2] ] += 1


trainFromStr(string)
print (wordBiGram)
print(letterBiGram)

# みんなのプログラムを参考に見ましたが、bi-gramって数える必要ないでしょうか？