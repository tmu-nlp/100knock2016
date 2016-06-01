import xml.sax as sax


class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = []

    def startElement(self, name, attrs):
        self.push_tag(name)

    def characters(self, content):
        if self.current_tag() == 'word':
            self.word = content
        if self.current_tag() == 'NER' and content == 'PERSON':
            print(self.word)

    def endElement(self, name):
        self.pop_tag()

    def current_tag(self):
        return self.tags[-1]

    def push_tag(self, tag):
        self.tags.append(tag)

    def pop_tag(self):
        return self.tags.pop(-1)


parser = sax.make_parser()
parser.setContentHandler(StanfordCoreXMLHandler())
parser.parse(open('nlp.xml'))
