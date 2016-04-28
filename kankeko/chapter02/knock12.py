#!-*-coding:utf-8-*-
#cat -f 1,2 hightemp.txt


list = open("hightemp.txt").readlines()
col1 = open("col1.txt","w")
col2 = open("col2.txt","w")

for list in list:
    list = list.expandtabs(1)
    list = list.split()
    col1.write(list[0] + "\n")
    col2.write(list[1] + "\n")
     
        
