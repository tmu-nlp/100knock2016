#'''
#python knock017.py col1.txt
#'''
#import sys
#
#d = dict()
#for line in open(sys.argv[1]):
#    d[line.strip()] = 0
#
#for key in d.keys():
#    print key

f=open("col1.txt","r")
s=f.read()
f.close()
d=dict()
for i in s.split("\n"):
    d[i]=0
for key in d.keys():
    print key
