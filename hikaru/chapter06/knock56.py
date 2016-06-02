from knock50 import getsentence
import re
from xml.etree import ElementTree

XMLFILE = "nlp.txt.out"
tree = ElementTree.parse(XMLFILE)
root = tree.getroot()

index_list = list()
temp_list = list()
coreference_coreferencelist = root.findall('.//coreference')
for coreference_coreference in coreference_coreferencelist:
    for coreference in coreference_coreference:
        textlist = coreference.findall('.//text')
        mentionlist = coreference.findall('.//mention')
        #wordlist = coreference.findall('.//word')
        for mention, text in zip(mentionlist, textlist):
            if mention.get("representative") == 'true':
                rep = text.text
                sentence_id = mention.find('.//sentence').text
                start_id = mention.find('.//start').text
                end_id = mention.find('.//end').text
                temp_list.append([rep, int(sentence_id), int(start_id), int(end_id)])
            else:
                sentence_id = mention.find('.//sentence').text
                start_id = mention.find('.//start').text
                end_id = mention.find('.//end').text
                temp_list.append(['{} ({})'.format(rep, text.text), int(sentence_id), int(start_id), int(end_id)])
temp_list.sort(key=lambda temp: int(temp[1]))
print (temp_list)
look = 0
#sentencelist = root.findall('.//sentence')
#for sentence in sentencelist:
    #token_list = sentence.findall('.//token')
    #word_list = sentence.findall('.//word')
    #for token, word in zip(token_list, word_list):
        #print (token.get("id"), word.text)
        #if sentence.get("id") == temp_list[look][1] and token.get("id") == temp_list[look][2]:
        #if sentence.get("id") == temp_list[look][1]:
            #print (sentence.get("id"))
            #print (temp_list[look][1])
            #look += 1
original = list()
sentencelist = root.findall('.//sentence')
for sentence in sentencelist:
    word_list = sentence.findall('.//word')
    original.append([word.text for word in word_list])
#print (original)
'''
ans = ''
flag1 = False
flag2 = False
for i, word_list in enumerate(original):
    for j, word in enumerate(word_list):
        for temp in temp_list:
            if (i+1) == temp[1]:
                if (j+1) >= temp[2] and (j+1) < temp[3]:
                    if flag1:
                        pass
                    else:
                        temp = temp[0] + ' '
                        ans += temp + ' '
                    flag1 = True
        if flag1:
            pass
        else:
            ans += word + ' '
        flag1 = False
    ans += '\n'
print (ans)
'''

for minitemp_list in reversed(temp_list):
    del original[minitemp_list[1]-1][minitemp_list[2]-1:minitemp_list[3]-1]
    original[minitemp_list[1]-1].insert(minitemp_list[2]-1, minitemp_list[0])
ans = ''
for sentence in original:
    for word in sentence:
        ans += word + ' '
    ans += '\n'
print (ans)



