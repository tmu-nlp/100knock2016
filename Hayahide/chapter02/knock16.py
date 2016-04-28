#-*- coding: utf-8 -*-

read = open("hightemp.txt", "r")
N = int(raw_input())
count = 0
line = 0
lists = []

for word in read:
    lists.append(word)
    line += 1

while count < N:
    ans = ""
    w_file = open("split%d.txt" % (count + 1), "w")
    if line % N != 0:
        temp = int(line / N) + 1
    else:
        temp = line / N
    for i in range(temp):
        if len(lists) == 0:
            break
        ans += lists.pop(0)
    w_file.write(ans)
    w_file.close()
    count += 1

read.close()

#UNIX command: split -l 10 hightemp.txt split_unix
