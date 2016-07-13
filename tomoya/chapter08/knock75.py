import sklearn.linear_model
from sklearn.externals import joblib

def getWorstTop_10():
    lr = joblib.load('./lr.pkl')
    dic2vec = joblib.load('dic2vec.pkl')
    with open('weight.txt', 'w') as fp:
        zipped = zip(dic2vec.get_feature_names(), *lr.coef_)
        weight_list = list()
        for feature, weight in sorted(zipped, key=lambda x: x[1]):
            weight_list.append("{}\t{}".format(feature, weight))
        worst10 = weight_list[:10]
        top10 = weight_list[-1:-11:-1]
        return top10, worst10
if __name__ == '__main__':
    top10, worst10 = getWorstTop_10()
    print("top10")
    print("\n".join(top10))
    print("\nworst10")
    print("\n".join(worst10))
