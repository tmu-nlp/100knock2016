from collections import defaultdict


def pair_counting():
    N = 0
    freq_tc = defaultdict(int)
    freq_t = defaultdict(int)
    freq_c = defaultdict(int)
    for line in open('knock82_context.txt', 'r'):
        words = line.strip('\n').split()
        freq_tc[words[0] + '\t' + words[1]] += 1
        N += 1
        freq_t[words[0]] += 1
        freq_c[words[1]] += 1

    return freq_tc, freq_t, freq_c, N

if __name__ == '__main__':
    freq_tc, freq_t, freq_c, N = pair_counting()
