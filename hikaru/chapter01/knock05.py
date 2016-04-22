#coding:UTF-8

def ngramW(n, str):
	ret = []
	str = str.split()
	str = list(str)
	for i in range(len(str) - n + 1):
		ret.append(tuple(str[i:i+n]))
	return ret

def ngramC(n, str):
    ret = []
    str2 = ""
    for cha in str:
        if cha != " ":
		    str2 += cha 
    for i in range(len(str2) - n + 1):
        ret.append(tuple(str[i:i+n]))
    return ret

print ngramW(2,"I am an NLPer")
print ngramC(2,"I am an NLPer")
