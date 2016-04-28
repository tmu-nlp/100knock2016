# -*- coding: utf-8 -*-


# n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# tango = []
#
# text = "I am an NLPer"
#
# words = text.split(" ")
#
# for i in range(len(words)-1):
#      tango.append(words[i:i+2])
#
# print(tango)
#
# moji = []
#
# text = "".join(words)
#chars = list(text)

#for i in range(len(chars)-1):
     #moji.append(chars[i:i+2])

#print(moji)

def n_gram(chars):
    moji = []
    for i in range(len(chars)-1):
         moji.append(chars[i:i+2])
    return moji

def main():
    text = "I am an NLPer"
    words = text.split(" ")
    moji = n_gram(words)

    print(moji)

    text = "".join(words)
    chars = list(text)
    moji = n_gram(chars)

    print(moji)

if __name__ == '__main__':
    main()
