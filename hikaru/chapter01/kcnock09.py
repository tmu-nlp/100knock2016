import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

word = str.split()
tango = []
result = []

for w in word: 
	if len(w) > 4:
		for t in w[1:-1]:
			tango.append(t)
		random.shuffle(tango)
		tango = ''.join(tango)
		tango = w[0] + tango + w[-1]
		result.append(tango)
		tango = []
	else:
		 result.append(w)

print result
