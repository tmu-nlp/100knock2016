f = open("hightemp.txt")
my_list = []
for line in f:
    line = line.split()
    my_list.append(line[0])
print (set(my_list))

# cat col1.txt|sort|uniq
