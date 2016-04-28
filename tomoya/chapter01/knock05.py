#coding: UTF-8
#
def ngram(s, n):
  t = []
  ans = []
  if isinstance(s, basestring): 
    t = s.replace(" ", "")
  if isinstance(s, list):
    for x in s: 
      t += x.split(" ")
  for i in range(len(t) - n + 1): 
     ans += [list(t[i:i +n])]
  return ans

print(ngram("I am an NLPer", 2))
print(ngram(["I am an NLPer"], 2))
    
