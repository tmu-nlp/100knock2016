string1 = "パトカー"
string2 = "タクシー"
strList =[]
for i in range(4):
	strList.append(string1[i])
	strList.append(string2[i])

string3 = "".join(strList)
print (string3)
