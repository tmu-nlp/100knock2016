def cipher(s):
	t = ''
	for i in range(len(s)):
		if s[i].islower():
			t+=chr(219-ord(s[i]))
		else:
			t+=s[i]

	return t

print(cipher("abcdEFGH"))
print(cipher(cipher("abcdEFGH")))
