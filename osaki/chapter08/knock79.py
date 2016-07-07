import sys
import matplotlib.pyplot as plt
from knock73 import rog_learn
from knock77 import acc_

pre=list()
rec=list()
thre=list()
d=rog_learn(10,open(sys.argv[1]))
for i in range(50):
    result=acc_(open(sys.argv[1]),d,i/100)
    pre+=[result[1]]
    rec+=[result[2]]
    thre+=[i]

plt.plot(thre,pre,label="precision",color="red")
plt.plot(thre,rec,label="recall",color="blue")
plt.show()
