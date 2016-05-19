#!/usr/bin/python
#_*_coding:utf-8_*_

import json


def get_UK_text():
    fin = open("jawiki-country.json", "r")
    for line in fin:
        jsonData = json.loads(line.strip().decode("utf-8"))
        if jsonData["title"] == u"イギリス":
            return jsonData["text"]


if __name__ == "__main__":
    print(get_UK_text())

