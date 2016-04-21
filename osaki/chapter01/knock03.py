s="Now I need a drink,alcoholic of course,after the heavy lectures involving quantum mechanics."
t=""
c=[]
for i in range(len(s)):
    if s[i]==" ":
        c=c+[len(t)]
        t=""
    elif s[i]==".":
        c=c+[len(t)]
        t=""
    elif s[i]==",":
        c=c+[len(t)]
        t=""
    else:
        t=t+s[i]

print(c)
