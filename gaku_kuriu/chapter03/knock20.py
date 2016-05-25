import sys, json

with open(sys.argv[1], 'r') as rf, open(sys.argv[2], 'w') as wf:
    for line in rf:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            wf.write(article['text'])
            print(article['text'])


