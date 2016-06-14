from knock41 import get_sentences
# cut -f1 knock47.txt| sort | uniq -c| sort -r | less
# cut -f1,2 knock47.txt| sort | uniq -c| sort -r | less

for sentence in get_sentences():
    for chunk in sentence:
        if chunk.has_verb():
            candidate = list()
            predicate = None
            for src_id in chunk.srcs:
                src_chunk = sentence[src_id]
                if src_chunk.is_sahen_wo():
                    predicate = src_chunk.join_surface() + chunk.get_most_left_verb()
                else:
                    part = src_chunk.get_most_right_particle()
                    if part is not None:
                        candidate.append((part, src_chunk.join_surface()))
            if predicate is not None and len(candidate) != 0:
                particles = ' '.join(part for part, ch in sorted(set(candidate)))
                chunks = ' '.join(ch for part, ch in sorted(set(candidate)))
                print('{}\t{}\t{}'.format(predicate, particles, chunks))
Status API Training Shop Blog About
