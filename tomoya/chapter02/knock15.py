#coding: utf-8
import sys
f_in = open("hightemp.txt", "r").readlines()
N = sys.argv[1]

for i in range(len(f_in) - int(N), len(f_in)):
        print(f_in[i], end='')

#flamie:chapter02 tomoya$ tail -n 4 hightemp.txt
#大阪府  豊中    39.9    1994-08-08
#山梨県  大月    39.9    1990-07-19
#山形県  鶴岡    39.9    1978-08-03
#愛知県  名古屋  39.9    1942-08-02
