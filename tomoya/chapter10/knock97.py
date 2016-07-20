from sklearn.cluster import KMeans
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
    km = KMeans(n_clusters=5)
    country = dictdata(getCountrydict())
    km.fit(country.getData())
    labels = km.labels_
    c_dict = country.linkage(labels)
    for country, c in sorted(c_dict.items(), key=lambda x: x[1]):
        print('{}:{}'.format(country, c))

if __name__ == '__main__':
    main()
