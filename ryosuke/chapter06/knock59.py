import xml.sax as sax
from nltk.tree import Tree


class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = list()

    def startElement(self, name, attrs):
        self.push_tag(name)

    def characters(self, content):
        if self.current_tag() == 'parse':
            tree = Tree.fromstring(content)
            for subtree in tree.subtrees():
                if subtree.label() == 'NP':
                    print(' '.join(subtree.leaves()))

    def endElement(self, name):
        self.pop_tag()

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
