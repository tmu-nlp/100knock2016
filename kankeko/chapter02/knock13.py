#!-*-coding:utf-8-*-
#paste -d "\t" col1.txt col2.txt

f = open("col3.txt",'w')
list = []
for (line1,line2) in zip(open("col1.txt", 'r'),open("col2.txt", 'r')):
    line1 = line1.strip()
    #line2 = line2.strip()
    list.append(line1)
    list.append(line2)
    f.write("\t".join(list))
    list = []   
