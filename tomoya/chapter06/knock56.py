import sys
import re
from collections import defaultdict

search_mention = re.compile('<mention>')
search_mention2 = re.compile('</mention>')
search_sentence = re.compile('<sentence>(.*)</sentence>')
search_start = re.compile('<start>(.*)</start>')
search_end = re.compile('<end>(.*)</end>')
search_sentence_id = re.compile('<sentence id="(.*)">')
search_word = re.compile('<word>(.*)</word>')
search_text = re.compile('<text>(.*)</text>')
search_head = re.compile('<head>(.*)</head>')
search_representative = re.compile('<mention representative="true">')
se = st = ed = hd = tt = None
#xml = defaultdict(list)
xml = []
rep_flag = False
for line in open("nlp.txt.out"):
    sentence_id = search_sentence_id.search(line)
    sentence = search_sentence.search(line)
    start = search_start.search(line)
    end = search_end.search(line)
    head = search_head.search(line)
    text = search_text.search(line)
    word = search_word.search(line)
    representative = search_representative.search(line)
    mention = search_mention.search(line)
    _mention = search_mention2.search(line)

    if sentence_id:
        s_id = sentence_id.group(1)
    elif word:
        if len(xml)  < int(s_id):
            xml.append([word.group(1)])
        else:
            xml[int(s_id) - 1].append(word.group(1))
    if representative:
        rep_flag = True
    elif mention:
        rep_flag = False
    if rep_flag:
        if text:
            tt = text.group(1)
    else:
        if sentence:
            se = sentence.group(1)
        elif start:
            st = start.group(1)
        elif end:
            ed = end.group(1)
        elif head:
            hd = head.group(1)
        elif _mention:
            xml[int(se) - 1][int(st) - 1] = "{} ( ".format(tt) + xml[int(se) - 1][int(st) - 1]
            xml[int(se) - 1][int(ed) - 1] = " ) " + xml[int(se) - 1][int(ed) - 1]

for sentence in xml:
    print(" ".join(sentence))
