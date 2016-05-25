# knock26.py
import sys
import re

pattern = re.compile(r"'{3,}")

for line in sys.stdin:
	newLine = pattern.sub("", line)
	print (newLine.strip())

# python3 knock20.py | python3 knock25.py | python3 knock26.py