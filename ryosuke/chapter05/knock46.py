from knock41 import get_sentences


for sentence in get_sentences():
    for chunk in sentence:
        if chunk.in_verb():
            candidate = list()
            for src_id in chunk.srcs:
                src_chunk = sentence[src_id]
                new_candidate = src_chunk.get_all_particles()
                if len(new_candidate) != 0:
                    candidate += [(part, src_chunk.join_surface()) for part in new_candidate]
            if len(candidate) != 0:
                verb = chunk.get_most_left_verb()
                particles = ' '.join(part for part, ch in sorted(set(candidate)))
                chunks = ' '.join(ch for part, ch in sorted(set(candidate)))
                print('{}\t{}\t{}'.format(verb, particles, chunks))
