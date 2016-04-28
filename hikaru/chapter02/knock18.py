from operator import itemgetter

f = open("hightemp.txt")
my_list = []
for line in f:
    line = line.split()
    list.append(line)
#print (my_list)
#print (my_list.sort(key=itemgetter(2)))
list = sorted(my_list, key=itemgetter(2))
print (my_list)
#list = sorted(my_list, key=lambda x: x[2])
#print (my_list)

# sort -r hightemp.txt

