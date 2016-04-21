hightemp = open('hightemp.txt').readlines()
N = int(input('ファイルをN分割: '))

def nbunkatsu(bun):
    k = round(len(hightemp)/bun)
    bos = 0
    eos = k

    def prnt(x,y):
        for line in range(x,y):
            print(hightemp[line].strip())
        print()

    prnt(bos,eos)

    while eos < len(hightemp) - k:
        bos += k
        eos += k
        prnt(bos,eos)
    else:
        bos += k
        eos = len(hightemp)
        prnt(bos,eos)

nbunkatsu(N)

