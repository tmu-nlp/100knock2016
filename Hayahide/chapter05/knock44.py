#-*- coding: utf-8 -*-
from knock43 import Morph, Chunk, Caboching, chunk_merge
from graphviz import Digraph

def merge(chunk):
    merge = ""
    for morph in chunk.morphs:
        if morph.pos != "記号":
            merge += morph.surface
    return merge

graph = Digraph(format = "png")
graph.attr("node", shape = "circle")

neko_list = Caboching()
line_num = 0
for line in neko_list:
    if line_num >= 10:
        break

    for chunk in line:
        graph.node(merge(chunk))
        if chunk.dst != -1:
            graph.edge(merge(chunk), merge(line[chunk.dst]))

    line_num += 1

print (graph)
graph.render("neko_tree")
