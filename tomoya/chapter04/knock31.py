#coding: utf-8
import sys
import re
morpheme = []
sentences = []
for line in open("neko.txt.mecab"):
  if "EOS" not in line:
    line_s = re.split("\s|,", line)
    morpheme.append({"surface": line_s[0], "base":line_s[7], "pos":line_s[1], "pos1":line_s[2]})
  elif morpheme != []:
    sentences.append(morpheme)
    morpheme = []
verb= []
for sentence in sentences:
  for word in sentence:
    if word["pos"] == u"動詞":
      verb.append(word["surface"])
print(verb)
