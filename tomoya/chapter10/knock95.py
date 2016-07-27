from scipy.stats import spearmanr
import numpy as np


def getSpearmanr(infile):
    x_list = list()
    y_list = list()
    for i, line in enumerate(open(infile, 'r')):
        words = line.strip('\n').split('\t')
        x_list.append((i, float(words[2])))
        y_list.append((i, float(words[3])))
    x_list = sorted(x_list, key=lambda x:x[1])
    y_list = sorted(y_list, key=lambda x:x[1])
    x_list = sorted([(x, i) for i, (x, score) in enumerate(x_list)], key=lambda x: x[0])
    y_list = sorted([(y, i) for i, (y, score) in enumerate(y_list)], key=lambda x: x[0])
    x_list, y_list = np.array(x_list), np.array(y_list)
    rho, pval = spearmanr(x_list[:, 1], y_list[:, 1])
    return rho, pval


def main():
    rho, pval = getSpearmanr('./knock85at94.data')
    print('knock85\nrho:{}\npval:{}'.format(rho, pval))
    rho, pval = getSpearmanr('./knock94.data')
    print('knock94\nrho:{}\npval:{}'.format(rho, pval))

if __name__ == '__main__':
    main()
