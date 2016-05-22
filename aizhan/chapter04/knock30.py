import re

def neko_mecab():
    mecab_list = []
    for line in open('neko.txt.mecab'):
        mecab_dic = {}
        line = line.strip()
        l = re.split(r',|\t',line)
        if 'EOS' in l:
            continue
        mecab_dic['surface'] = l[0] if l[0] != '*' else ''
        mecab_dic['base'] = l[-3] if l[-3] != '*' else ''
        mecab_dic['pos'] = l[1] if l[1] != '*' else ''
        mecab_dic['pos1'] = l[2] if l[2] != '*' else ''
        mecab_list.append(mecab_dic)
    return mecab_list

if __name__ == '__main__':
    print(neko_mecab())

