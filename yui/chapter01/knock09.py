# -*- coding: utf-8 -*-


# Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually
# understand what I was reading : the phenomenal power of the human
# mind ."）を与え，その実行結果を確認せよ．

# 標準ライブラリ「random」（あとで、random.shuffle()使用）
import random

if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    shuf_sentence = list()
    for char in sentence.split():
        if len(char) <= 4:
            shuf_sentence.append(char)
        else:
            head = char[0]
            middle = list(char[1:-1])
            tail = char[-1]
            random.shuffle(middle)
            char = "%s%s%s" % (head, "".join(middle), tail)
            shuf_sentence.append(char)
    print " ".join(shuf_sentence)

