s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Maight Also Sign Pease Security Clause. Arthur King Can. "
n=[1,5,6,7,8,9,15,16,19]
d={}
a=1
t=""
for i in range(len(s)):
        if s[i]==" ":
                if a in n:
                        d[t[:1]]=str(a)
                else:
                        d[t[:2]]=str(a)
                a=a+1
                t=""

        else:
                t=t+s[i]

print(d)
