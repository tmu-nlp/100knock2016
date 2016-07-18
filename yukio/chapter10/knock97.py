from knock96 import extract_countries
from sklearn.cluster import KMeans

countries = []
vectors = []
for country, vector in sorted(extract_countries().items()):
    countries.append(country)
    vectors.append(vector)

model = KMeans(n_clusters = 5).fit(vectors)

result = [[], [], [], [], []]

for country, label in zip(countries, model.labels_):
    result[label].append(country)

for i, group in enumerate(result):
    print(i)
    print("\n".join(group))
    print()
