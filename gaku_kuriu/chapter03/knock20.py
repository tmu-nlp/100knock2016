import sys, json

rf = open(sys.argv[1], 'r')
wf = open(sys.argv[2], 'w')

for line in rf:
    article = json.loads(line)
    if article['title'] == 'イギリス':
        json.dump(article['text'], wf)
        print(article['text'])

rf.close()
wf.close()


