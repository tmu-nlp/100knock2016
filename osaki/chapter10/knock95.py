def cal_sp(f1,f2):
    d_f1=dict()
    d_f2=dict()
    d_list=dict()
    for (line1,line2) in zip(f1,f2):
        d_f1["\t".join(line1.split()[:2])]=line1.strip("\n").split()[2]
        d_f2["\t".join(line2.split()[:2])]=line2.strip("\n").split()[2]
        d_list["\t".join(line1.split()[:2])]="\t".join(line1.split()[:2])
    f1_rank=mk_rank(d_f1)
    f2_rank=mk_rank(d_f2)
    N=len(d_list)
    D=0
    for key,value in d_list.items():
        D+=(f1_rank[key]-f2_rank[key])**2
    rho=1-6*D/(N**3-N)
    return rho

def mk_rank(d):
    d_rank=dict()
    for key,value in sorted(d.items(),key=lambda x:x[1],reverse=True):
        d_rank[key]=len(d_rank)
    return d_rank

if __name__=="__main__":
    print("10  "+str(cal_sp(open("knock94_10.txt","r"),open("wordsim353/set1.tab","r"))))
    print("09  "+str(cal_sp(open("knock94_09.txt","r"),open("wordsim353/set1.tab","r"))))
