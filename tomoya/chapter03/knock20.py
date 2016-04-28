#coding: utf-8
import sys
import json
f_in = open("jawiki-country.json", "r")
#f_out = open("UK.txt", "w")
for line in f_in:
  jsonData = json.loads(line)
  if jsonData["title"] == u"イギリス":
    print("{}\n{}".format(jsonData["title"], jsonData["text"]))
   # f_out.write(jsonData["text"])
f_in.close()
#f_out.close()
