#-*- coding: utf-8 -*-

read = open("hightemp.txt", "r")

my_dict = {}

for line in read:
    line = line.strip()
    word = line.split()
    
    if word[0] in my_dict:
        my_dict[word[0]] += 1
    elif word[0] not in my_dict:
        my_dict[word[0]] = 1

for key, value in sorted(my_dict.items(), key = lambda x:x[1], reverse = True):
    print ("%s %r" % (key, value))



