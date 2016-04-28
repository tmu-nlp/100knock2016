f1 = open("col1.txt")
f2 = open("col2.txt")

f = open("knock13.txt", "w")
for line1, line2 in zip(f1, f2):
    line1 = line1.strip()
    f.write(line1)

    f.write("\t")
    f.write(line2)
    #f.write("\n")

# paste col1.txt col2.txt
