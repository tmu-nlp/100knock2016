import sys
with open("hightemp.txt", "r") as f:

    bunkatsu_list = []
    for (i, line) in enumerate(f):
        line = line.split()
    i = i + 1
    if (i % int(sys.argv[1])) == 0:
        for j in range(int(sys.argv[1])):
            bunkatsu_list.append(i / int(sys.argv[1]))
            #print ("owata")
    else:
        amari = i % int(sys.argv[1])
        for j in range(int(sys.argv[1]) - amari):
            bunkatsu_list.append(int(i / int(sys.argv[1])))
        for j in range(amari):
            bunkatsu_list.append(int(i / int(sys.argv[1]))+1)
    count = 0
    bunkatsu = bunkatsu_list[count]
    lines = []
with open("hightemp.txt", "r") as f:
    for (number, line) in enumerate(f):
        if number < bunkatsu:
            lines.append(line + '\n')
            open("knock16-{}".format(count+1, "w").write(lines)
            #open("knock16-{}".format(count+1), "a").write(line)
            if number+1 == bunkatsu:
                if number+1 != i:
                    count += 1
                    bunkatsu += bunkatsu_list[count]
                    #print ("/n")    
