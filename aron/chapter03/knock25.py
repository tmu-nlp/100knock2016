# knock25.py
import sys;
import re
pattern = re.compile(r"^\{基礎情報.*")
pattern2 = re.compile(r"\|[^\|]*=[^\|]*\|")
lst = []
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
				print (m.group(0))
				m2 = re.findall(pattern2, m.group(0))
				# print (m2)
				print (len(m2))
				for item in m2:
					print (item)
	if(len(lst) == 0):
		print ("finish")
	else:
		print ("unfinish")

	# print (line)