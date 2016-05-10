# knock08.py
def cipher(str_in):
	newStr = list()
	for ch in str_in:
		if ch >='a' and ch <= 'z':
			newStr.append((chr)(219 - ord(ch)))
		else: 
			newStr.append(ch)
	return "".join(newStr)

print(cipher("zzz"))
