def cal_ac(f1,f2):
    c=0
    t=0
    for (line1,line2) in zip(f1,f2):
        c+=1
        if line1.split()[4]==line2.split()[3]:
            t+=1
    return t/c

print("09 "+str(cal_ac(open("knock92_09.txt","r"),open("knock91.txt","r"))))
print("10 "+str(cal_ac(open("knock92_10.txt","r"),open("knock91.txt","r"))))
