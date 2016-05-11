import gzip
import json


def getUKtext():
    for line in gzip.open('jawiki-country.json.gz'):
        d = json.loads(line.decode('utf-8'))
        if d['title'] == 'イギリス':
            return d['text']

if __name__ == '__main__':
    print(getUKtext())
