#coding: UTF-8
import knock05 as k5
x = "paraparaparadise"
y = "paragraph"
X = set(k5.ngram(x, 2))
Y = set(k5.ngram(y, 2))
U = X.union(Y)
V = X.intersection(Y)
W1 = X.difference(Y)
W2 = Y.difference(Y)
print(U)
print(V)
print(W1)
print(W2)
def isIncluded(x):
  if x: print("is included")
  else: print("is not included")

isIncluded(set(["se"]).issubset(X))
isIncluded(set(["se"]).issubset(Y))