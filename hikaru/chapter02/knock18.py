from operator import itemgetter

f = open("hightemp.txt")
my_list = []
for line in f:
    line = line.split()
    my_list.append(line)
#print (my_list)
#print (my_list.sort(key=itemgetter(2)))
#list = sorted(my_list, key=itemgetter(2))
#print (my_list)
#list = sorted(my_list, key=lambda x: x[2])
my_list2 = sorted(my_list, key=lambda x: x[2],reverse = True)
for line in my_list2:
    print (line)
# sort -rk 3 hightemp.txt

