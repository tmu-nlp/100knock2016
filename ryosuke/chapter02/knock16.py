import sys


def split_list(l, num):
    size = len(l)
    base = size // num
    remaining = size % num
    outerl = list()
    start = 0
    for i in range(num):
        additional = 1 if remaining > 0 else 0
        remaining -= 1
        innerl = l[start:start + base + additional]
        start += base + additional
        outerl.append(innerl)
    return outerl

num = int(sys.argv[1])
all_line = list()
for line in open('hightemp.txt'):
    all_line.append(line.rstrip('\n'))

for i, lines in enumerate(split_list(all_line, num)):
    fw = open('spl{}.txt'.format(i), 'w')
    for line in lines:
        print(line, file=fw)

# 妥協
# spl -l 4 hightemp.txt
