# -*- coding: utf-8 -*-

import cgi
import cgitb
from pymongo import MongoClient

cgitb.enable()

client = MongoClient()
db = client.artist_db
col = db.artist_col

form = cgi.FieldStorage()

query = dict()
if 'name' in form:
    query['name'] = form['name'].value
    print("query")
if 'aliases_name' in form:
    query['aliases_name'] = form['aliases_name'].value
    print("query")
if 'tag' in form:
    query['tag'] = form['tag'].value
    print("query")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello % Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello </h2>")
print("</body>")
print("</html>")
