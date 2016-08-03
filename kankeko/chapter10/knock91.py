#knock91.txt

flag = 0
for line in open("questions-words.txt"):
    words = line.strip('\n')
    if ":" in words:
        if flag == 1:
            exit()
    if words in ": family":
        flag = 1
        continue
    if flag == 1:
        print(words)
