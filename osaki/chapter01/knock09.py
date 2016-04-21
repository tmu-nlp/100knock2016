import random

u=[]
sf=[]
t=""
tf=""
tm=""
tl=""
s="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
for t in s.split():
    if len(t)<=4:
        u.append(t)
    else:
        tf=t[0]
        tl=t[-1]
        sf=list(t[1:-1])
        random.shuffle(sf)
        t=tf+tm.join(sf)+tl
        u.append(t)

print(" ".join(u))
