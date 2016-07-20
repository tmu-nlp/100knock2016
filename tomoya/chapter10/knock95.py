from scipy.stats import spearmanr


def getSpearmanr(infile):
    x_list = list()
    y_list = list()
    for line in open(infile, 'r'):
        words = line.strip('\n').split('\t')
        x_list.append(float(words[2]))
        y_list.append(float(words[3]))
    rho, pval = spearmanr(x_list, y_list)
    return rho, pval


def main():
    rho, pval = getSpearmanr('./knock85at94.data')
    print('knock85\nrho:{}\npval:{}'.format(rho, pval))
    rho, pval = getSpearmanr('./knock94.data')
    print('knock94\nrho:{}\npval:{}'.format(rho, pval))

if __name__ == '__main__':
    main()
