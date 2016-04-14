#coding: utf-8

s1 = u"パトカー"
s2 = u"タクシー"
s3 = s1 + s2

a = ""
for i in range(len(s1)):
    a = a + s1[i:i+1:]
    a = a + s2[i:i+1:]
print a
