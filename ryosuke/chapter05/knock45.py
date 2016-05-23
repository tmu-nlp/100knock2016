from knock41 import get_sentences
# sort knock45.txt | uniq -c | sort -r | less
# grep -e 'する' -e '見る' -e '与える' knock45.txt| sort | uniq -c | sort -r | less

for sentence in get_sentences():
    for chunk in sentence:
        if chunk.has_verb():
            candidate = list()
            for src_id in chunk.srcs:
                src_chunk = sentence[src_id]
                part = src_chunk.get_most_right_particle()
                if part is not None:
                    candidate.append(part)
            if len(candidate) != 0:
                verb = chunk.get_most_left_verb()
                particles = ' '.join(sorted(set(candidate)))
                print('{}\t{}'.format(verb, particles))
