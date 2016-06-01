import re


def make_sentence():
    ans_list = []
    temp = []
    for line in open("knock53_out.txt", "r"):
        temp.append(line.strip("\n"))
        if re.match("[\.;:\?!]", line):
            ans_list.append(temp)
            temp = []
    return ans_list

nlp_list = make_sentence()
cor_start = re.compile("<coreference>")
cor_end = re.compile("</coreference>")
ment_start = re.compile("<mention>")
ment_rep = re.compile("<mention representative=.*>")
ment_end = re.compile("</mention>")

flag = False
start = 0
end = 0
sentence = ""
for line in open("nlp.txt.out", "r"):
    sentence_check = re.search("<sentence>(?P<sentence_id>\d+)</sentence>", line)
    head_check = re.search("<head>(?P<head_id>\d+)</head>", line)
    text_check = re.search("<text>(?P<text_data>.*)</text>", line)
    start_check = re.search("<start>(?P<start_id>\d+)</start>", line)
    end_check = re.search("<end>(?P<end_id>\d+)</end>", line)

    if ment_rep.search(line):
        flag = True
    elif flag and text_check:
        text = text_check.group("text_data")
    elif flag == False:
        if sentence_check:
            sentence = nlp_list[int(sentence_check.group("sentence_id")) - 1]
        elif start_check:
            start = int(start_check.group("start_id")) - 1
        elif end_check:
            end = int(end_check.group("end_id")) - 1
        elif len(sentence[start:end]) > 0:
            before_text = " ".join(sentence[start:end])
            del sentence[start:end]
            sentence.insert(start, text + "(" + before_text + ")")
            print (" ".join(sentence))
            sentence = ""
            start = 0
            end = 0
    elif cor_end.search(line):
        before_text = ""

    elif flag and ment_end.search(line):
        flag = False 
