#coding: utf-8
import sys
import re
from collections import defaultdict
morpheme = []
sentences = []
for line in open("neko.txt.mecab"):
  if "EOS" not in line:
    line_s = re.split("\s|,", line)
    morpheme.append({"surface": line_s[0], "base":line_s[6], "pos":line_s[1], "pos1":line_s[2]})
  elif morpheme != []:
    sentences.append(morpheme)
    morpheme = []
dic = []
norm = defaultdict(str)
prenorm = defaultdict(str)
postnorm = defaultdict(str)
flag = False
for sentence in sentences:
  for word in sentence:
    prenorm = norm
    norm = postnorm
    postnorm = word
    if norm["surface"] == "の" and prenorm["pos"] == "名詞" and postnorm["pos"] == "名詞":
      dic.append(prenorm["surface"] + "の" + postnorm["surface"])
print(dic)
