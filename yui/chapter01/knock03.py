# -*- coding: utf-8 -*-


# 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures
# involving quantum mechanics."という文を単語に分解し，各単語の
# （アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．


sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# made an empty list to put numbers later.
sw = []

# split sentence into word strings.
ss = sentence.split(" ")

# made a loop for ss. count length of each word and put them in
# the list sw.
for word in ss:
    # strip away ,. from word.
    wws = word.strip(",.")
    # count length of words and put the result into sw.
    sw.append(len(wws))

print(sw)
