from knock96 import extract_countries
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

countries = []
vectors = []
for country, vector in sorted(extract_countries().items()):
    countries.append(country)
    vectors.append(vector)

model = TSNE()
new_vectors = model.fit_transform(vectors)

fig, ax = plt.subplots()
ax.scatter(new_vectors[:, 0], new_vectors[:, 1])
for index, label in enumerate(countries):
    ax.annotate(label, xy=(new_vectors[index, 0], new_vectors[index, 1]))
plt.show()
