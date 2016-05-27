import sys
import re
def getSentence():
  searchPause = re.compile("(.*)[\.;\:\?!]\s([A-Z].*)", re.DOTALL)
  sentence = list()
  sentences = list()
  for line in open("nlp.txt"):
    target = searchPause.search(line)
    if target:
      sentence.append(target.group(1))
      sentences.append("".join(sentence))
      sentence = []
      sentence.append(target.group(2))
    else:
      sentence.append(line)
  return sentences

if __name__ == "__main__":
  sentences = getSentence()
  for sentence in sentences:
    print("<s>{}</s>".format(sentence))
    
