#coding: utf-8
import re
import requests
from knock20 import uktext
from collections import defaultdict

temp = re.compile("\|(.*)\s=\s(.*)")
emphasis = re.compile("'")
internallink = re.compile(r"\[\[.*?:*\s*(.*?)\]\]")
others = re.compile("\*")
template = dict()
for line in uktext().split("\n"):
  line = emphasis.sub("", line)
  line = internallink.sub(r"\1", line)
  line = others.sub(" ", line)
  target = temp.search(line)
  if target:
    template[target.group(1)] = target.group(2)
imgname = template[u"国旗画像"]
url = "https://en.wikipedia.org/w/api.php?action=query&titles=File:{}&prop=imageinfo&&iiprop=url&format=json".format(imgname)
req = requests.get(url).json()
print(req["query"]["pages"]["".join(req["query"]["pages"].keys())]["imageinfo"][0]["url"])
