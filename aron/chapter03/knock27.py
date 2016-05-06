# knock27.py
import sys
import re

pattern = re.compile(r"^\{基礎情報 国\\n\|(.*)\\n}$")
pattern2 = re.compile(r"^(.*) = (.*)$")
# re3 = re.compile(r"\[\[([\[\]\|]*)\|([\[\]\|]*)\]\]")
re3 = re.compile(r"\[\[[^\[\]]*\|([^\[\]]*)\]\]")
re4 = re.compile(r"\[\[([^\[\]]*)\]\]")
lst = []
dic = dict();
# num = 0;
for line in sys.stdin:
	for (i, ch) in enumerate(line):
		if ch == '{':
			lst.append(i)
		elif ch == '}':
			start = lst.pop()
			subStr = line[start: i + 1]
			# print (subStr)
			m = pattern.match(subStr)
			if(m):
				# print (m.group(1))
				lst2 = m.group(1).split(r"\n|")
				for item in lst2:
					m2 = re.findall(pattern2, item)
					# print (item)
					# print (len(m2))
					for item2 in m2:
						dic[item2[0]] = item2[1]
						# print ("%s =|= %s" % (item2[0], item2[1]))



						newStr1 = re3.sub(r"\1", item2[1])
						newStr2 = re4.sub(r"\1", newStr1)
						# if m3:
						# 	for i, mm in enumerate(m3) :
						# 		print (i , mm)
						# else:
						# 	print (item2[1])
						print (item2[0], "=", newStr2)