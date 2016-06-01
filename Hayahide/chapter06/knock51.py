import re
cmpl = re.compile("[\.;:\?!,]")

for sentence in open("knock50_output.txt", "r"):
    line = cmpl.sub("", sentence).split()
    for word in line:
        print(word)
    print("\n")
