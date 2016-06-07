import xml.dom.minidom
from nltk.tree import *


def getNodes(tree):
    for node in tree.subtrees(filter=lambda x: x.label() == 'NP'):
        print(node, '\n')


def s_expression_analysis():
    dom = xml.dom.minidom.parse("nlp.txt.xml")
    parses = dom.getElementsByTagName('parse')
    for prs in parses:
        tree_prs = prs.firstChild.data
        tree = Tree.fromstring(tree_prs)
        getNodes(tree)


if __name__ == '__main__':
    s_expression_analysis()
