a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

list = a.split()
element = {}

for (i, x) in enumerate(list):
    if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
        element[i+1] = x[0]
    else:
        element[i+1] = x[0]+x[1]
print (element)
	
