s1 = 'パトカー'
s2 = 'タクシー'

s = ''
for t1, t2 in zip(s1, s2):
    s += t1
    s += t2
print(s)
