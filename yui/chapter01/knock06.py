# -*- coding: utf-8 -*-

#集合
#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
#それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
#さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

# 先に書いたknock05の（n_gram）を持ってくる。
import knock05 as get_n_gram

# 関数を定義する。
def main():
    text = "paraparaparadise"
    x = get_n_gram.n_gram(list(text))
    print(x)
    difx = dif(x)
    print(difx)

    text = "paragraph"
    y = get_n_gram.n_gram(list(text))
    print(y)
    dify = dif(y)
    print(dify)

    union = (difx | dify)
    intersection = (difx & dify)
    difference = (difx - dify)

    print(union)
    print(intersection)
    print(difference)

    if "se" in difx:
        print (u"found_se_in_x")
    if "se" in dify:
        print (u"found_se_in_y")



def dif(bi_grams):
    dif_bi_grams = set()
    for bi_gram in bi_grams:
        dif_bi_grams.add("".join(bi_gram))
    return dif_bi_grams


if __name__ == '__main__':
    main()
