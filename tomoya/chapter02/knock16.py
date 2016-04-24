#coding: utf-8
import sys
N = sys.argv[1]
line_sum = sum(1 for line in open("hightemp.txt"))
quotient = int(line_sum / int(N))
remainder = line_sum % int(N)
loop_num = [quotient]*int(N)
for i in range(remainder):
        loop_num[i] += 1
f_in = open("hightemp.txt", "r").readlines()
f_out = open("output.txt", "w")
i = count = 0
for line in f_in:
        if (count >= loop_num[i]):
                f_out = open("output{}.txt".format(i + 1), "w")
                count = 0
                i += 1
        f_out.write(line)
        count += 1
f_out.close()

#flamie:chapter02 tomoya$ split -l 5 hightemp.txt
