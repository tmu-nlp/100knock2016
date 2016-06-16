# knock69.py
# coding = utf-8

# import pymongo
import http.server,os
import webbrowser
# os.system('open http://127.0.0.1:5000/')

#この行以降の行が実行されない
http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler)

os.system("http://localhost:8000/cgi-bin/knock69.cgi")
# webbrowser.open("http://localhost:8000/cgi-bin/knock69.cgi")

