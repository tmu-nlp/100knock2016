#!/Users/ryosuke/.pyenv/versions/myenv3.5.1/bin/python

import cgi
from pymongo import MongoClient
from pymongo import DESCENDING

def print_html():
    html = '''
    <html>
    <head>
    <title>Python CGI Test</title>
    </head>

    <body>
    <h1>Python CGI Test</h1><hr><p>

    <form name = "Form1" method="post" action="./knock069.cgi">
    name: <input type="text" size=30 name="name"><p>
    aliases_name: <input type="text" size=30 name="aliases_name"><p>
    tag: <input type="text" size=30 name="tag"><p>
    <input type="submit" value="submit" name="button1"><p>
    </form>
    <hr>
    </body>
    </html>
    '''
    print('Content-Type: text/html\n\n')
    print(html)


def print_result(query):
    # connection
    client = MongoClient()
    db = client['100knock']
    collection = db['artist']
    # find
    results = list()
    for data in collection.find(query, sort=[('rating.count', DESCENDING)], limit=10):
        results.append(data)
    if len(results) == 0:
        print('There is no Artist')
    else:
        for i, data in enumerate(results):
            print(i)
            print('<br>')
            print(data)
            print('<br>')

# get form info
form = cgi.FieldStorage()
query = dict()
if 'name' in form:
    query['name'] = form['name'].value
if 'aliases_name' in form:
    query['aliases.name'] = form['aliases_name'].value
if 'tag' in form:
    query['tags.value'] = form['tag'].value


print_html()
if len(query.keys()) != 0:
    print_result(query)

