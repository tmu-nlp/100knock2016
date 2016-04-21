#coding: utf-8

text = "I am an NLPer".split()

num1 = len(text)-1

for i in range(num1):
    print str(text[i]) + "-" + str(text[i+1])   
    
for i in text:
    if len(i) != 1:
        num2 = len(i)-1
        for j in range(num2):
            print str(i[j]) + "-" + str(i[j+1])
            
        




