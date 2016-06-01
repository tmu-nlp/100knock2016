from collections import defaultdict
import xml.sax as sax


class SVOSlot:
    def __init__(self):
        self.s = None
        self.v = None
        self.o = None

    def is_filled(self):
        return self.s is not None and self.v is not None and self.o is not None

    def fill_s(self, s):
        self.s = s

    def fill_v(self, v):
        self.v = v

    def fill_o(self, o):
        self.o = o

    def get_svo(self):
        return self.s, self.v, self.o


class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = list()
        self.in_dependencies = False
        self.vid2svo = defaultdict(SVOSlot)
        self.already = set()

    def startElement(self, name, attrs):
        self.push_tag(name)
        if name == 'sentence' and 'id' in attrs:
            self.sent_id = attrs['id']
        if name == 'dependencies' and \
                'type' in attrs and attrs['type'] == 'collapsed-dependencies':
            self.in_dependencies = True
        if self.in_dependencies and name == 'dep' and 'type' in attrs:
            self.type = attrs['type']
        if self.in_dependencies and name == 'governor':
            self.gov_id = '{}_{}'.format(self.sent_id, attrs['idx'])

    def characters(self, content):
        if self.in_dependencies:
            if self.current_tag() == 'governor':
                if self.gov_id in self.already:
                    pass
                else:
                    svo = self.vid2svo[self.gov_id]
                    if self.type == 'nsubj':
                        svo.fill_v(content)
            if self.current_tag() == 'dependent':
                if self.gov_id in self.already:
                    pass
                else:
                    svo = self.vid2svo[self.gov_id]
                    if self.type == 'nsubj':
                        svo.fill_s(content)
                        if svo.is_filled():
                            print('{}\t{}\t{}'.format(*svo.get_svo()))
                            self.vid2svo[self.gov_id] = None
                            self.already.add(self.gov_id)
                    elif self.type == 'dobj':
                        svo.fill_o(content)
                        if svo.is_filled():
                            print('{}\t{}\t{}'.format(*svo.get_svo()))
                            self.vid2svo[self.gov_id] = None
                            self.already.add(self.gov_id)

    def endElement(self, name):
        self.pop_tag()
        if name == 'dependencies':
            self.is_representative = False

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
