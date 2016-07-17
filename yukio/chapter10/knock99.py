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

plt.scatter([vec[0] for vec in new_vectors], [vec[1] for vec in new_vectors]) 
plt.show()
