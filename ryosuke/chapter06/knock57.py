import os
import shutil
import xml.sax as sax
from graphviz import Digraph


class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = list()
        self.graph = Digraph(format='svg')
        self.in_dependencies = False

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
        if self.in_dependencies and name == 'dependent':
            self.dep_id = '{}_{}'.format(self.sent_id, attrs['idx'])

    def characters(self, content):
        if self.in_dependencies:
            if self.current_tag() == 'governor':
                self.graph.node(self.gov_id, content)
            if self.current_tag() == 'dependent':
                self.graph.node(self.dep_id, content)
                self.graph.edge(self.dep_id, self.gov_id, label=self.type)

    def endElement(self, name):
        self.pop_tag()
        if name == 'dependencies':
            self.is_representative = False
            fname = '{}/{}'.format(dirname, self.sent_id)
            self.graph.render(fname, cleanup=True)
            self.graph = Digraph(format='svg')

    def current_tag(self):
        return self.tags[-1]

    def push_tag(self, tag):
        self.tags.append(tag)

    def pop_tag(self):
        return self.tags.pop(-1)

dirname = './img_knock57'
if os.path.exists(dirname):
    shutil.rmtree(dirname)
os.mkdir(dirname)

parser = sax.make_parser()
handler = StanfordCoreXMLHandler()
parser.setContentHandler(handler)
parser.parse(open('nlp.xml'))
