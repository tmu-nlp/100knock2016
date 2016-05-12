#coding: utf-8
import sys
import json
def uktext():
  for line in open("jawiki-country.json", "r"):
    jsonData = json.loads(line)
    if jsonData["title"] == u"イギリス":
      return(jsonData["text"])

if __name__ == "__main__":
  print(uktext())
