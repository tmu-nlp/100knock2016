#-*- coding: utf-8 -*-

r1 = open("col1.txt", "r")
temp1 = r1.read()
r1.close()
text1 = temp1.split("\n")

r2 = open("col2.txt", "r")
temp2 = r2.read()
r2.close()
text2 = temp2.split("\n")

merge = ""
count = 0

for line in range(len(text1)):
    merge = merge + text1[count] + "\t" + text2[count] + "\n"
    count += 1

w = open("col_merge.txt", "w")
w.write(merge)
w.close()

#UNIX command: paste col1_unix.txt col2_unix.txt > merge_unix.txt
