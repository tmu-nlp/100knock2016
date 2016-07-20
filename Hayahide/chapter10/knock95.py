import sys


def Spearman(human_rank, model_rank):
    sigma = 0
    for key, rank in sorted(model_rank.items(), key=lambda x: x[1]):
        D = rank - human_rank[key]
        sigma += D ** 2
    return 1 - 6 * sigma / (len(model_rank) ** 3 - len(model_rank))


def ranker(f):
    human_sim = dict()
    model_sim = dict()
    for line in open(f, 'r'):
        words = line.strip('\n').split()
        human_sim[len(human_sim)] = float(words[2])
        model_sim[len(model_sim)] = float(words[3])

    human_rank = dict()
    for key, value in sorted(human_sim.items(), key=lambda x: x[1]):
        if value != 0:
            human_rank[key] = len(human_rank)

    model_rank = dict()
    for key, value in sorted(model_sim.items(), key=lambda x: x[1]):
        if value != 0:
            model_rank[key] = len(model_rank)

    print("Spearman's Correlation: {}".format(Spearman(human_rank, model_rank)))

if __name__ == '__main__':
    for f in sys.argv[1:]:
        ranker(f)
