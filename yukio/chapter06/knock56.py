import re

pattern_sentence = re.compile('<sentence id="(?P<sentence_id>[0-9]+)">')
pattern_token = re.compile('<token id="(?P<token_id>[0-9]+)">')
pattern_word = re.compile("<word>(?P<word>.+)</word>")
i = 0
j = 0
document = []

pattern_start = re.compile('<coreference>')
pattern_end = re.compile('</coreference>')
pattern_mention_rep = re.compile('<mention representative="true"')
pattern_mention_notrep = re.compile('<mention>')
pattern_mention_end = re.compile('</mention>')
pattern_text = re.compile("<text>(?P<text>.+)</text>")
pattern_sentence_id = re.compile("<sentence>(?P<sentence_id>.+)</sentence>")
pattern_start_id = re.compile("<start>(?P<start_id>.+)</start>")
pattern_end_id = re.compile("<end>(?P<end_id>.+)</end>")
coref_check = False
mention_rep_check = False
mention_notrep_check = False
representative = ""
k = 0
l_start = 0
l_end = 0

for line in open("nlp.txt.xml", "r"):
    if re.search(pattern_sentence, line):
        i = int(re.search(pattern_sentence, line).group("sentence_id")) - 1
        document.append([])
    elif re.search(pattern_token, line):
        j = int(re.search(pattern_token, line).group("token_id")) - 1
        document[i].append("")
    elif re.search(pattern_word, line):
        document[i][j] = re.search(pattern_word, line).group("word")

    elif re.search(pattern_start, line):
        coref_check = True
    elif re.search(pattern_end, line):
        coref_check = False
        representative = ""

    elif coref_check:
        if re.search(pattern_mention_rep, line):
            mention_rep_check = True
        elif re.search(pattern_mention_notrep, line):
            mention_notrep_check = True
        elif re.search(pattern_mention_end, line):
            mention_rep_check = False
            mention_notrep_check = False
            k = 0
            l_start = 0
            l_end = 0
        elif mention_rep_check and re.search(pattern_text, line):
            representative = str(re.search(pattern_text, line).group("text"))
        elif mention_notrep_check:
            if re.search(pattern_sentence_id, line):
                k = int(re.search(pattern_sentence_id, line).group("sentence_id")) - 1
            elif re.search(pattern_start_id, line):
                l_start = int(re.search(pattern_start_id, line).group("start_id")) - 1
            elif re.search(pattern_end_id, line):
                l_end = int(re.search(pattern_end_id, line).group("end_id")) - 1
                document[k].insert(l_end, ")")
                document[k].insert(l_start, "(")
                words = representative.split()
                words.reverse()
                for word in words:
                    document[k].insert(l_start, word)


for sentence in document:
    print(" ".join(sentence))

            

    
