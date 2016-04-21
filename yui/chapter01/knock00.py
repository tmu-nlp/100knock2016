#-*- coding:utf-8 -*-

#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

#文字列'stressed'をAと定義する。
A = 'stressed'
#Aのlengthをlength_of_Aとする。
length_of_A = len(A)

#リストを作成
list_of_A = []
#length_of_Aの範囲のiに対して、
for i in range(length_of_A):
    ##iは何か確認するためprintしてみる。
    ##print i

    #先に作ったリストにA('stressed')の要素('s''t''r'...)を追加していく。
    ##append:リストの最後に引数に指定したオブジェクトを追加する。
    list_of_A.append(A[i])

#先に作ったリスト(list_of_A)をreverse_list_of_Aと定義する。
reverse_list_of_A = list_of_A
#リスト(list_of_A)の要素を逆順に並べる
##printすると、'd''e'...
reverse_list_of_A.reverse()

#上で逆順に並べ替えた要素を一つの文字列にする。
##join:文字列シーケンスの連結(.joinの前の部分''は区切り文字列。この場合、各要素間に区切り文字は不要なので''のみとなっている。)
B = ''.join(reverse_list_of_A)

print(B)
