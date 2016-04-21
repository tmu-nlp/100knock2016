a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

a = a.replace(",", "")
a = a.replace(".", "")
l = a.split()

for i in range(len(l)):
	l[i] = len(l[i])
print (l)	
