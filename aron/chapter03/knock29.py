# knock29.py
import sys, re, json, urllib.request, urllib.parse
flag_name = "Flag of the United Kingdom.svg"
wiki_url = "https://en.wikipedia.org/w/"
api_url = "api.php?action=query&prop=imageinfo&format=json&iiprop=url&titles=File:"
url = wiki_url + api_url + urllib.parse.quote(flag_name)
# print("urle")
response = urllib.request.urlopen(wiki_url + api_url + urllib.parse.quote(flag_name))
wikijson = json.loads(response.read().decode('utf-8'))
print(wikijson)
# print(wikijson['query']['pages']['23473560']['imageinfo'][0]['url'])
