import xml.sax as sax
from collections import defaultdict


class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = list()
        self.sentences = list()
        self.correferences = defaultdict(list)
        self.is_mention = False
        self.is_representative = False

    def startElement(self, name, attrs):
        self.push_tag(name)
        if name == 'sentence' and 'id' in attrs:
            self.sentence = list()
            self.sentences.append(self.sentence)
        if name == 'mention':
            if 'representative' in attrs:
                self.is_representative = True
            else:
                self.is_mention = True

    def characters(self, content):
        if self.current_tag() == 'word':
            self.sentence.append(content)
        if self.is_representative and self.current_tag() == 'text':
            self.representative = content
            self.is_representative = False
        if self.is_mention:
            if self.current_tag() == 'sentence':
                self.sentence_id = int(content) - 1
            if self.current_tag() == 'start':
                self.start = int(content) - 1
            if self.current_tag() == 'end':
                self.end = int(content) - 1
                self.correferences[self.sentence_id].append((self.start, self.end, self.representative))

    def endElement(self, name):
        self.pop_tag()
        if name == 'mention':
            self.is_mention = False

    def current_tag(self):
        return self.tags[-1]

    def push_tag(self, tag):
        self.tags.append(tag)

    def pop_tag(self):
        return self.tags.pop(-1)

parser = sax.make_parser()
handler = StanfordCoreXMLHandler()
parser.setContentHandler(handler)
parser.parse(open('nlp.xml'))

for i, sentence in enumerate(handler.sentences):
    for start, end, representative in sorted(handler.correferences[i], key=lambda x: -x[1]):
        sentence.insert(end, ')')
        sentence.insert(start, '(')
        sentence.insert(start, representative)
    print(' '.join(sentence))
