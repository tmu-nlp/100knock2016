import xml.dom.minidom
from nltk.tree import *


def getNodes(parent):
    for node in parent:
        for i in node.subtrees(filter=lambda x: x.label() == 'NP'):
            print(i, '\n')


def s_expression_analysis():
    dom = xml.dom.minidom.parse("nlp.txt.xml")
    parses = dom.getElementsByTagName('parse')
    for prs in parses:
        tree_prs = prs.firstChild.data
        tree = Tree.fromstring(tree_prs)
        getNodes(tree)


if __name__ == '__main__':
    s_expression_analysis()
