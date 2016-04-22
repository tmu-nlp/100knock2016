#-*- coding: utf-8 -*-

r = open("hightemp.txt", "r")

temp = r.read()
r.close()
temp = temp.replace("\t", " ")
w = open("hightemp_space.txt", "w")
w.write(temp)

w.close()

#UNIX command: tr "\t" " " < hightemp.txt > text_space_unix.txt
