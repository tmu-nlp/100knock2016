from graphviz import Digraph
import xml.dom.minidom


def dependency_parsing():
    dom = xml.dom.minidom.parse("nlp.txt.xml")
    dpnds = dom.getElementsByTagName('dependencies')
    dot = Digraph(format='png')
    idgov, iddep, lblgov, lbldep = '', '', '', ''
    for dpnd in dpnds:
        if dpnd.getAttribute('type') == "collapsed-dependencies":
            deps = dpnd.getElementsByTagName('dep')
            for dep in deps:
                governors = dep.getElementsByTagName('governor')
                dependents = dep.getElementsByTagName('dependent')
                for governor, dependent in zip(governors, dependents):
                    idgov = governor.getAttribute('idx')
                    lblgov = governor.firstChild.data
                    iddep = dependent.getAttribute('idx')
                    lbldep = dependent.firstChild.data
                    dot.node(str(iddep), lbldep)
                    dot.node(str(idgov), lblgov)
                    dot.edge(str(iddep), str(idgov))
            dot.render('png-knock57', cleanup=True)
            exit()


if __name__ == '__main__':
    dependency_parsing()
