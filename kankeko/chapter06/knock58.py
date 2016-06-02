import xml.dom.minidom


def dependency_parsing():
    dom = xml.dom.minidom.parse("nlp.txt.xml")
    dpnds = dom.getElementsByTagName('dependencies')
    nsubj_g, nsubj_d, dobj_g, dobj_d = [], [], [], []
    predicaten, predicated = [], []
    for dpnd in dpnds:
        if dpnd.getAttribute('type') == "collapsed-dependencies":
            deps = dpnd.getElementsByTagName('dep')
            for dep in deps:
                if dep.getAttribute('type') == "nsubj":
                    nsubj_g = dep.getElementsByTagName('governor')
                    nsubj_d = dep.getElementsByTagName('dependent')
                if dep.getAttribute('type') == "dobj":
                    dobj_g = dep.getElementsByTagName('governor')
                    dobj_d = dep.getElementsByTagName('dependent')
            for nsj in nsubj_g:
                predicaten.append(nsj.firstChild.data)
            for dbj in dobj_g:
                predicated.append(dbj.firstChild.data)
            for i,pn in enumerate(predicaten):
                for j,pd in enumerate(predicated):
                    if pn == pd:
                        print(pn + "\t" + nsubj_d[i].firstChild.data + "\t" + dobj_d[j].firstChild.data)
        predicated=[]
        predicaten=[]


if __name__ == '__main__':
    dependency_parsing()
