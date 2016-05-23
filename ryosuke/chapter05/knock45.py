from knock41 import get_sentences
# sort knock45.txt | uniq -c | sort -r | less
# grep -e 'する' -e '見る' -e '与える' knock45.txt| sort | uniq -c | sort -r | less

for sentence in get_sentences():
    for chunk in sentence:
        if chunk.in_verb():
            candidate = list()
            for src_id in chunk.srcs:
                src_chunk = sentence[src_id]
                candidate += src_chunk.get_all_particles()
            if len(candidate) != 0:
                particles = ' '.join(sorted(set(candidate)))
                print('{}\t{}'.format(chunk.get_most_left_verb(), particles))
