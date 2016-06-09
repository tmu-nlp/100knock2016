from knock41 import get_sentences
import itertools


def get_path(n1, n2, sentence):
    if n2.id < n1.id:
        n1, n2 = n2, n1
    n1path = n1.get_path_to_root(sentence, form=lambda ch: ch.id)
    # same path
    if n2.id in n1path:
        def get_x2y(ch):
            if ch.id == n1.id:
                return ch.replace_noun('X')
            if ch.id == n2.id:
                return ch.replace_noun('Y')
            return ch.join_surface_wo_symbol()
        return '->'.join(n1.get_path_to_id(sentence, n2.id, form=get_x2y))
    
    # branched path
    def get_replaced(XorY, id):
        def replace(ch):
            if ch.id == id:
                return ch.replace_noun(XorY)
            return ch.join_surface_wo_symbol()
        return replace
    n2path = n2.get_path_to_root(sentence, form=lambda ch: ch.id)
    first_shared_id = min(set(n1path) & set(n2path))
    n1path = '->'.join(n1.get_path_to_id(sentence, first_shared_id, form=get_replaced('X', n1.id), include_id=False))
    n2path = '->'.join(n2.get_path_to_id(sentence, first_shared_id, form=get_replaced('Y', n2.id), include_id=False))
    return '|'.join([n1path, n2path, sentence[first_shared_id].join_surface_wo_symbol()])


for sentence in get_sentences():
    noun_phrases = [ch for ch in sentence if ch.has_noun()]
    noun_pairs = itertools.combinations(noun_phrases, 2)
    for n1, n2 in noun_pairs:
        print(get_path(n1, n2, sentence))