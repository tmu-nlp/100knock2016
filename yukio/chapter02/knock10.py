# -*- coding: utf-8 -*-

i = 0
for s in open("hightemp.txt", "r"):
    i += 1
print("{}行".format(i))

# wc -l hightemp.txt
