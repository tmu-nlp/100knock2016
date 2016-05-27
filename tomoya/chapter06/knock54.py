import sys
import re

word = re.compile("<word>(.*)</word>")
lemma = re.compile("<lemma>(.*)</lemma>")
pos = re.compile("<POS>(.*)</POS>")
tag = list()

for line in open("nlp.txt.out"):
  search_word = word.search(line)
  search_lemma = lemma.search(line)
  search_pos = pos.search(line)
  if search_word:
    print(search_word.group(1), end = "\t")
  elif search_lemma:
    print(search_lemma.group(1), end = "\t")
  elif search_pos:
    print(search_pos.group(1))

