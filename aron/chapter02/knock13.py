# knock13.py
import sys

# col = int(sys.argv[1]) - 1


my_file1 = open('col1.txt', "r")
my_file2 = open('col2.txt', "r")

for (line1, line2) in zip(my_file1, my_file2):
	print (line1.strip() + "\t" + line2.strip())


'''
linux command
paste col1.txt col2.txt
'''
