s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

s = s.replace(".", "")
s = s.split(" ");
t = []
for (i, x) in enumerate(s):
	if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
	  t.append((x[:1], i))
	else:
	  t.append((x[:2], i))
s = {x: y for x, y in t}
print(s)