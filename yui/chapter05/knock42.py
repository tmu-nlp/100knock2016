# -*- coding: utf-8 -*-

#42. 係り元と係り先の文節の表示
#係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．


from knock41 import get_sentences

for sentence in get_sentences():
    for chunk in sentence:
        if chunk.dst != 1:
            src = chunk.join_surface_wo_symbol()    #係り元文節表層形文字列
            dst = sentence[chunk.dst].join_surface_wo_symbol()  #係り先文節表層形文字列
            if src == " or dst == ":            #記号をぬいたことによって、何もなくなっている文節がないかどうかチェック。
                continue
            print('{}\t{}'.format(src, dst))    
