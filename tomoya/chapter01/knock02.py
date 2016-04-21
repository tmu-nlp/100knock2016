#coding: UTF-8
s = u"パトカー"
t = u"タクシー"
u = ""
for i in range(max(len(s), len(t))):
  if i < len(s): 
    u += s[i]
  if i < len(t):
    u += t[i]
print(u)
  
