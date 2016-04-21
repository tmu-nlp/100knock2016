def cipher(str):
	results = ""
	for tango in str:
		if ord("a") <= ord(tango) <= ord("z"):
			results += chr(219 - ord(tango))
		else:
			results += tango
	return results

X = "100pon KnoCk"
print cipher(X)
print cipher(cipher(X))
