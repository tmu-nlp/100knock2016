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
    countries = dictdata(getCountrydict())
    result = model.fit_transform(countries.getData())
    hidden, graph = plt.subplots()
    graph.scatter(result[:, 0], result[:, 1], s=1)
    for i, country in enumerate(countries.getName()):
        graph.annotate(country, xy=(result[i, 0], result[i, 1]), size=10)
    plt.show()

if __name__ == '__main__':
    main()
