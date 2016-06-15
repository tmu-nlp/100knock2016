#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import http.server
import webbrowser

if __name__ == "__main__":
    webbrowser.open("http://localhost:8000/cgi-bin/import_knock69.py")
else:
    def make_searchscreen():
        print('Content-Type: text/html; charset=UTF-8\r\n')
        print('<head>')
        print('<title>アーティスト情報検索</title>')
        print('<link rel="stylesheet" type="text/css" href="../default.css">')
        print('</head>')
        print('<body>')
        print('<h1>アーティスト情報検索</h1>')
        print('<form action="import_knock69.py" method = "post">')
        print('<p>')
        print('<input type="text" name="text" size="80" style="font-size:15px;">')
        print('</p>')
        print('<p>')
        print('<input type="radio" name="field" value="name" checked="checked">アーティスト名で検索')
        print('<input type="radio" name="field" value="aliases.name">アーティスト別名で検索')
        print('<input type="radio" name="field" value="tags.name">タグで検索')
        print('<input type="radio" name="field" value="area">活動場所で検索')
        print('</p>')
        print('<p>')
        print('<input type="radio" name="query_type" value="1" checked="checked">部分一致')
        print('<input type="radio" name="query_type" value="2">完全一致')
        print('上位<input type="text" name="lim" size="5" value="20">件')
        print('<input type="submit" value="検索">')
        print('</p>')
        print('</form>')
        print('</body>')

    def make_resultscreen(text, field, lim, query_type):
        client = pymongo.MongoClient()
        db = client.MusicBrainz_DB
        collection = db.artist_collection

        print('Content-Type: text/html; charset=UTF-8\r\n')
        print('<head>')
        print('<title>アーティスト情報検索</title>')
        print('<link rel="stylesheet" type="text/css" href="../default.css">')
        print('</head>')
        print('<body>')
        print('<h1>アーティスト情報検索</h1>')
        print('<form action="import_knock69.py" method = "post">')
        print('<p>')
        print('<input type="text" name="text" value="')
        print(text)
        print('" size="80" style="font-size:15px;">')
        print('</p>')
        print('<p>')
        print('<input type="radio" name="field" value="name"')
        if field == "name":
            print(' checked="checked"')
        print('>アーティスト名で検索')
        print('<input type="radio" name="field" value="aliases.name"')
        if field == "aliases.name":
            print(' checked="checked"')
        print('>アーティスト別名で検索')
        print('<input type="radio" name="field" value="tags.value"')
        if field == "tags.value":
            print(' checked="checked"')
        print('>タグで検索')
        print('<input type="radio" name="field" value="area"')
        if field == "area":
            print(' checked="checked"')
        print('>活動場所で検索')
        print('</p>')
        print('<p>')
        print('<input type="radio" name="query_type" value="1"')
        if query_type == "1":
            print(' checked="checked"')
        print('>部分一致')
        print('<input type="radio" name="query_type" value="2"')
        if query_type == "2":
            print(' checked="checked"')
        print('>完全一致')
        print('上位<input type="text" name="lim" size="5" value="')
        print(lim)
        print('">件')
        print('<input type="submit" value="検索">')
        print('</p>')
        print('</form>')
        print('<p></p>')
        print('<h1>')
        if field == "name":
            print('アーティスト名　"')
        elif field == "aliases.name":
            print('アーティスト別名　"')
        elif field == "tags.value":
            print('タグ　"')
        elif field == "area":
            print('活動場所　"')
        print(text)
        print('"　検索結果　(')
        if query_type == "1":
            print('部分一致')
        else:
            print('完全一致')
        print('上位')
        print(lim)
        print('件)')
        print('</h1>')
        if query_type == "1":
            query = {"$regex": text}
        else:
            query = text
        if collection.find({field: query}, {"name": 1, "aliases": 1, "tags": 1, "area": 1, "begin": 1, "end": 1, "rating": 1, "_id": 0}).count() != 0:
            print('<p>')
            print('<table id="result" align="center" width="80%">')
            print('<tr>')
            print('<th width="5%"></th>')
            print('<th width="15%">アーティスト名</th>')
            print('<th width="20%">別名</th>')
            print('<th width="20%">タグ</th>')
            print('<th width="10%">活動場所</th>')
            print('<th width="10%">活動開始</th>')
            print('<th width="10%">活動終了</th>')
            print('<th width="10%">レーティング</th>')
            print('</tr>')
            for i, line in enumerate(collection.find({field: query}, {"name": 1, "aliases": 1, "tags": 1, "area": 1, "begin": 1, "end": 1, "rating": 1, "_id": 0}).sort("rating.count", -1).limit(int(lim))):
                print('<tr>')
                print('<td>')
                print(i + 1)
                print('</td>')
                for key in ["name", "aliases", "tags", "area", "begin", "end", "rating"]:
                    print('<td>')
                    if key in line:
                        if isinstance(line[key], str):
                            print(line[key])
                        elif isinstance(line[key], dict):
                            cell = []
                            if "year" in line[key]:
                                cell.append("{}年".format(line[key]["year"]))
                            if "month" in line[key]:
                                cell.append("{}月".format(line[key]["month"]))
                            if "date" in line[key]:
                                cell.append("{}日".format(line[key]["date"]))
                            if "count" in line[key]:
                                cell.append(str(line[key]["count"]))
                            print("".join(cell))
                        elif isinstance(line[key], list):
                            cell = []
                            for line2 in line[key]:
                                if "value" in line2:
                                    cell.append(line2["value"])
                                elif "name" in line2:
                                    cell.append(line2["name"])
                            print(", ".join(cell))
                    else:
                        print('')
                    print('</td>')
                print('</tr>')
            print('</table>')
            print('</p>')
        else:
            print('<h2>検索結果がありません</h2>')
        print('</body>')
