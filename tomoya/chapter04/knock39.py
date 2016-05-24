#coding: utf-8
import sys
import re
from collections import defaultdict
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
morpheme = []
sentences = []
for line in open("neko.txt.mecab"):
  if "EOS" not in line:
    line_s = re.split("\s|,", line)
    morpheme.append({"surface": line_s[0], "base":line_s[6], "pos":line_s[1], "pos1":line_s[2]})
  elif morpheme != []:
    sentences.append(morpheme)
    morpheme = []
count = defaultdict(int)
for sentence in sentences:
  for word in sentence:
    count[word["surface"]] += 1
y = []
for k, v in sorted(count.items(), key = lambda x:x[1], reverse = True):
  y.append(v)
plt.xscale("log")
plt.yscale("log")
x = range(1,len(y)+1)
plt.plot(x, y)
plt.show()
 
