
#coding: utf-8

a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()

dict = {}
check=0
key = [1, 5, 6, 7, 8, 9, 15, 16, 19]
for num,i in enumerate(a):
    num += 1
    for j in key:
        if  num == j:
            dict[i[:1]] = num
            check=1
    if check == 0:
        dict[i[:2]] = num
    check=0

print dict
            


