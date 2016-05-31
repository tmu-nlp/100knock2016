import sys
import re

word = re.compile("<word>(.*)</word>")
person = re.compile("<NER>PERSON</NER>")
for line in open("nlp.txt.out"):
  search_word = word.search(line)
  search_person = person.search(line)
  if search_word:
    word_person = search_word.group(1)
  elif search_person:
    print(word_person)
    word_person = None

