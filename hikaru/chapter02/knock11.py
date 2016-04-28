f = open("hightemp.txt")
for line in f: 
    print (line.replace("\t", " "))


#expand -t 4 hightemp.txt
