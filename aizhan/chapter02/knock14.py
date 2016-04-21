N = int(input('先頭からN行: '))

def sentoun(gyou):
    count = 0
    hightemp = open('hightemp.txt').readlines()
    for line in range(0,gyou):
        print(hightemp[line].strip())

sentoun(N)

