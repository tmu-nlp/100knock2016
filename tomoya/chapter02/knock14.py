#coding: utf-8
import sys
f_in = open("hightemp.txt", "r")
N = sys.argv[1]
for i, line in zip(range(int(N)), f_in):
        print(line, end='')
f_in.close()

#flamie:chapter02 tomoya$ head -n 4 hightemp.txt
#高知県  江川崎  41  2013-08-12
#埼玉県  熊谷    40.9    2007-08-16
#岐阜県  多治見  40.9    2007-08-16
#山形県  山形    40.8    1933-07-25
