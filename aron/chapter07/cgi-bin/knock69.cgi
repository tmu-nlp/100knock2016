#!/usr/local/bin/python3
import cgi, pymongo

def loadHtml(path):
    print('Content-type: text/html; charset=UTF-8\r\n')

    with open(path, "r") as html:
        for line in html:
            print(line.strip() + "\r\n")



def queryData(data):
    client = pymongo.MongoClient()
    db = client['artistdb']
    collection = db['artist']
    results = list()
    for data in collection.find(data, sort=[('rating.count', pymongo.DESCENDING)], limit=10):
        results.append(data)
    print('%d 件の結果<br>' % (len(results)))
    print("<ol>")
    for i, data in enumerate(results):

        print('<li>')
        # print("<h4>%d</h4>" % (i))
        # print("<hr>")
        print(data)
        print('</li>')
    print("</ol>")


# postしたデータを取得
def getData():
    form = cgi.FieldStorage()
    post = dict()
    if 'artist_name' in form:
        post['name'] = form['artist_name'].value
    if 'artist_alias' in form:
        post['aliases.name'] = form['artist_alias'].value
    if 'artist_tag' in form:
        post['tags.value'] = form['artist_tag'].value
    if(len(post.keys()) > 0):
        return post
    else:
        return None
# loadHtml("./index.html")

if __name__ == '__main__':
    # main()
    loadHtml("./index.html")
    data = getData()
    if data != None:
        queryData(data)