def ngramC(n, str):
        ret = []
        str2 = ""
        for cha in str:
                if cha != " ":
                        str2 += cha
        for i in range(len(str2) - n + 1):
                ret.append(tuple(str2[i:i+n]))
        return ret

X = ngramC(2,"paraparaparadise")
Y = ngramC(2,"paragraph")
X = set(X)
Y = set(Y)

print X | Y 
print X & Y
print X - Y
print X.issuperset([('s', 'e')])
print Y.issuperset([('s', 'e')])
