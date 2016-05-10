# knock16.py

# 自然数Nをコマンドライン引数などの手段で受け
# 取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ

'''
split 
'''

import sys


N = int(sys.argv[1])
base = sys.argv[2]
my_file = open('hightemp.txt', "r")

count = 0;
for i, line in  enumerate(my_file):
	if(i % N == 0):
		out_file = open(("%s%02d%s" % (base, count, ".txt")), "w")
		count += 1
	if(i % N  < N - 1):
		out_file.write(line)
	else:
		out_file.write(line.strip())