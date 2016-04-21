#coding: utf-8

text1 = "paraparaparadise"
text2 = "paragraph"

def check(text):
    list = []
    num = len(text)-1
    for i in range(num):
        list.append(str(text[i:i+1]) + str(text[i+1:i+2]))
    return list

list1 = set(check(text1))
list2 = set(check(text2))
print list1
print list2

print list1.union(list2)
print list1.intersection(list2)
print list1.difference(list2)

print "se" in list1.union(list2)



