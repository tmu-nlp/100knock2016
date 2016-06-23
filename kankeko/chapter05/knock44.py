import sys
from graphviz import Digraph
from knock41 import get_sentences


def sent2graph(sentence):
    dot = Digraph(format='png')
    for chunk in sentence:
        if chunk.dst != -1:
            dot.node(str(chunk.id), chunk.join_surface())
            dot.node(str(chunk.dst), sentence[chunk.dst].join_surface())
            dot.edge(str(chunk.id), str(chunk.dst))
    dot.render('knock44')


target = int(sys.argv[1]) - 1
for i, sentence in enumerate(get_sentences()):
    if i == target:
        sent2graph(sentence)
        break
