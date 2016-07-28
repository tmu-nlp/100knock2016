import numpy as np
from sklearn.cluster import KMeans
from knock96 import countries_dict


features = []
for key, value in sorted(countries_dict.items()):
    features.append(value)

kmeans_model = KMeans(n_clusters=5, random_state=10).fit(features)

labels = kmeans_model.labels_

for label, country in sorted(zip(labels, sorted(countries_dict))):
    print(label, country)
