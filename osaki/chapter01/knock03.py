s="Now I need a drink,alcoholic of course,after the heavy lectures involving quantum mechanics."
c=[]
s=s.replace(","," ")
s=s.replace("."," ")
for i in s.split():
    c=c+[len(i)]

print(c)
