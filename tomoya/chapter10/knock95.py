from scipy.stats import spearmanr


def getSpearmanr(infile):
    x_list = list()
    y_list = list()
    for line in open(infile, 'r'):
        words = line.strip('\n').split('\t')
        x_list.append(float(words[2]))
        y_list.append(float(words[3]))
    p, r = spearmanr(x_list, y_list)
    return p, r


def main():
    p, r = getSpearmanr('./knock85at94.data')
    print('knock85\np:{}\nr:{}'.format(p, r))
    p, r = getSpearmanr('./knock94.data')
    print('knock94\np:{}\nr:{}'.format(p, r))

if __name__ == '__main__':
    main()
