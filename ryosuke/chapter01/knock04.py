s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
indexes = [1, 5, 6, 7, 8, 9, 15, 16, 19]
indexes = [i - 1 for i in indexes]

d = dict()
for i, tok in enumerate(s.split()):
    if i in indexes:
        key = tok[0]
    else:
        key = tok[:2]
    d[key] = i
print(sorted(d.items(), key=lambda x: x[1]))
