import sys, re, json, urllib.request, urllib.parse

ansdict = {}

def filter(s):
    if re.search('\[{2}.*\]{2}', s):
        if re.search('\[{2}(.*?)\|(.*?)\]{2}', s):
            s = re.sub('\[{2}[^\[\]]*?\|(.*?)\]{2}', '\\1', s)
        else:
            s = re.sub('\[{2}(.*?)\]{2}', '\\1', s)
        return(filter(s))
    else:
        return(s)

with open(sys.argv[1], 'r') as rf:
    s = rf.read()
    splits = re.split('\n[\|\}]', s)
    for sp in splits:
        result = re.search('(.*)\s\=\s(.*)', sp, re.DOTALL)
        if result != None:
            ansdict[result.group(1)] = filter(re.sub("['{2}'{3}'{5}]", '', result.group(2)))


            
filename = ansdict['国旗画像']
wikiurl = 'https://en.wikipedia.org/w/'
wikiapi = 'api.php?action=query&prop=imageinfo&format=json&iiprop=url&titles=File:'

response = urllib.request.urlopen(wikiurl + wikiapi + urllib.parse.quote(filename))
wikijson = json.loads(response.read().decode('utf-8'))
print(wikijson['query']['pages']['23473560']['imageinfo'][0]['url'])

