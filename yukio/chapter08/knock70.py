import random

document = []

for line in open("rt-polaritydata/rt-polarity.pos", "rb"):
    document.append("+1 " + line.decode("latin-1"))
for line in open("rt-polaritydata/rt-polarity.neg", "rb"):
    document.append("-1 " + line.decode("latin-1"))

random.shuffle(document)

f = open("sentiment.txt", "w")
f.write("".join(document))
f.close()

#cut -b1 sentiment.txt | sort | uniq -c
