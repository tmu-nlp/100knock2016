from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import ward, dendrogram
from knock96 import getCountrydict
from matplotlib.pyplot import show


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
    wr = AgglomerativeClustering(linkage='ward', n_clusters=5)
    country = dictdata(getCountrydict())
    wr.fit(country.getData())
    result = ward(country.getData())
    dendrogram(result, labels=country.getName(), orientation='left')
    show()

if __name__ == '__main__':
    main()
