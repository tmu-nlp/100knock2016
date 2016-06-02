import xml.dom.minidom


def corefer_analysis():
    mr_text, m_text = '', ''
    dom = xml.dom.minidom.parse("nlp.txt.xml")
    corefs = dom.getElementsByTagName('coreference')
    for coref in corefs:
        mentions = coref.getElementsByTagName('mention')
        for mention in mentions:
            if mention.getAttribute('representative') == "true":
                mr_text = mention.getElementsByTagName('text')[0].firstChild.data
            else:
                m_text = mention.getElementsByTagName('text')[0].firstChild.data
            if m_text == '':
                continue
            print('[' + mr_text + '(' + m_text + ')' + ']')


if __name__ == '__main__':
    corefer_analysis()
