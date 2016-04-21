S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
L = S.split()
Lkeys = []
Lvalues = []
for i,w in enumerate(L):
    if i in [0,4,5,6,7,8,14,15,18]:
        Lvalues.append(w[0])
        Lkeys.append(i+1)
    else:
        Lvalues.append(w[:2])
        Lkeys.append(i+1)
D = dict(zip(Lkeys, Lvalues))
print(D)

