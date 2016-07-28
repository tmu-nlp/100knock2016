import numpy as np
from knock96 import countries_dict
from scipy.cluster.hierarchy import ward,dendrogram
from matplotlib.pyplot import show

features = []
country_names = []

for key, value in countries_dict.items():
    features.append(value)
    country_names.append(key)

ward_result = ward(features)
dendrogram(ward_result, labels=country_names)
show()
