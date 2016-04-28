#-*- coding: utf-8 -*-

read = open("hightemp.txt", "r")
N = int(raw_input())
count = 0
ans = []  
for lines in read:
    if count >= N:
        ans.pop(0)
    else:
        count += 1
    ans.append(lines.rstrip())

read.close()

for i in ans:
    print i

#UNIX command: tail -n 3 hightemp.txt
#山梨県  大月    39.9    1990-07-19
#山形県  鶴岡    39.9    1978-08-03
#愛知県  名古屋  39.9    1942-08-02
