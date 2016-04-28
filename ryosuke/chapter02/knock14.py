import sys

for _, line in zip(range(int(sys.argv[1])), open('hightemp.txt')):
    print(line.rstrip('\n'))

# head -n4 hightemp.txt
