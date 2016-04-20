N = int(input('末尾のN行: '))
 
def matsubi(gyou):
    hightemp = open('hightemp.txt').readlines()
    for line in range(len(hightemp)-gyou,len(hightemp)):
         print(hightemp[line].strip())
        
matsubi(N)

