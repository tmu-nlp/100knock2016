#expand -t 1 hightemp.txt

hightemp = open('hightemp.txt')
newline = ''

for line in hightemp:
    for i in line:
        if i == '\t':
            newline = newline + ' '
        else:
            newline = newline + i 

print(newline)

