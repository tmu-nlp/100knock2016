f = open("hightemp.txt")
f1 = open("col1.txt", "w")
f2 = open("col2.txt", "w")
for line in f.readlines():
  line = line.split()
  f1.write(line[0])
  f1.write("\n")
  f2.write(line[1])
  f2.write('\n')

# cut -f2 hightemp.txt
