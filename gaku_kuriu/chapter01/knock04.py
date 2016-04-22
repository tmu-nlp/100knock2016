import re

s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
timing = [1, 5, 6, 7, 8, 9, 15, 16, 19]
answer = {}

wordlist = re.sub('[.,]', '', s).split(' ')

for i in range(len(wordlist)):
    if i+1 in timing:
        answer[wordlist[i][:1]] = i+1
    else:
        answer[wordlist[i][:2]] = i+1

print(answer)
        
    
