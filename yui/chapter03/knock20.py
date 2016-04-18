# -*- coding: utf-8 -*-


# JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を
# 表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．


import json

# "open" is a function
f = open("jawiki-country.json", "r")
# "readlines" is a method
#print open("jawiki-country.json").readlines()[1][0]

#ひとつのものになってたから、各列を一旦一つ一つ読み込まなければならない。
#それからやりたいことをコードする。
# Data = json.loads(f.readlines()[0])

#元のファイルを読んで、各ラインをstringにする？
for json_line in f.readlines():
    a = json.loads(json_line)

    #タイトルがイギリスと同じだったらそれに該当する本文をエンコードしてプリンと。
    if a["title"] == u"イギリス":
        print a["text"].encode("utf-8")
        break

# for a in Data:
#     if a["title"] == u"イギリス":
#         print a["text"].encode("utf-8")
#         break

#ひとつのものになってたから、各列を一旦一つ一つ読み込まなければならない。
#それからやりたいことをコードする。
