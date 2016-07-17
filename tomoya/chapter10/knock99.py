from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from knock96 import getCountrydict


class dictdata:
    def __init__(self, dic):
        self.name = []
        self.data = []
        for key, value in sorted(dic.items(), key=lambda x: x[0]):
            self.name.append(key)
            self.data.append(value)
            self.classification = {}

    def getName(self):
        return self.name

    def getData(self):
        return self.data

    def linkage(self, labels):
        for name, cluster in zip(self.name, labels):
            self.classification[name] = cluster
        return self.classification


def main():
    model = TSNE(n_components=2)
    country = dictdata(getCountrydict())
    result = model.fit_transform(country.getData())
    print(result)
    plt.plot(result[:, 0], result[:, 1], ".")
    # plt.scatter(result[:, 0], result[:, 1], cmap=plt.cm.Spectral)
    plt.show()

if __name__ == '__main__':
    main()
