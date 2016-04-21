#coding: UTF-8
def ngram(s, n):
  t = []
  ans = []
  if isinstance(s, basestring): 
    t = s.replace(" ", "")
  if isinstance(s, list):
    for x in s: 
      t += x.split(" ")
  for i in range(len(t) - n + 1): 
     ans += [t[i:i +n]]
  #print(ans)
  return ans

ngram("I am an NLPer", 2)
ngram(["I am an NLPer"], 2)
    
