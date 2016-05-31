# knock50.py
# coding = utf-8
import sys, re
reg = re.compile("(?<=[\.;:\?\!]) (?=[A-Z\n])")

file = open("nlp.txt", "r")
def iterLine(input):
	# li = input.split("\n")
	for line in input:
		# line.rstrip()
		match = reg.split(line.rstrip())
		# print (match)
		if match:
			for m in match:
				yield m
		else:
			yield m

def main():
	input = object()
	if sys.stdin.isatty() == False:	# 標準入力からの入力
		input = sys.stdin
	else:
		input = open(sys.argv[1], "r")
	for line in iterLine(input):
		print(line)
if __name__ == '__main__':
	main()