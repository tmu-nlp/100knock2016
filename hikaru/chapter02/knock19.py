f = open("hightemp.txt")
my_dict = {}
my_list = []
for line in f:
    line = line.split()
    my_list.append(line[0])
for word in my_list:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

for foo, bar in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
    print("{} ---> {}".format(foo, bar))

# cat col1.txt|sort
