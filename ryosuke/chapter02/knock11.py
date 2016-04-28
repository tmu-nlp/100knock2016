for line in open('hightemp.txt'):
    print(line.replace('\t', ' ').rstrip('\n'))

# sed -e 's/    / /g' hightemp.txt
# cat hightemp.txt | tr '\t' ' '
# expand -t 1 hightemp.txt
