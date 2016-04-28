f = open("hightemp.txt")

print (sum(1 for (i, line) in enumerate(f)))
    
# US wc -l [filename]
