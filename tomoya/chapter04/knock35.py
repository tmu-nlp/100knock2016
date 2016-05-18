#coding: utf-8
import sys
import re
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
norm = []
norms = []
for sentence in sentences:
  for word in sentence:
    if word["pos"] == "名詞":
      norm.append(word["surface"])
    else:
      if len(norm) >= 2:
        norms.append("".join(norm))
      norm = []
print(norms)
