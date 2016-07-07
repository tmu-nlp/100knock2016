from knock76 import getLabeledData

def get_eval(prediction, reference):
    accuracy = sum(p == r for p, r in zip(prediction, reference)) / len(prediction)
    cor = sum(p == r == 1 for p, r in zip(prediction, reference))
    precision = cor / sum(p == 1 for p in prediction)
    recall = cor / sum(r == 1 for r in reference)
    F1 = 2 * precision * recall / (precision + recall)
    return accuracy, precision, recall, F1

if __name__ == '__main__':
    ref, pred, prob = getLabeledData()
    accuracy, precision, recall, F1 = get_eval(pred, ref)
    print("accuracy:{0:.3f}".format(accuracy))
    print("precision:{0:.3f}".format(precision))
    print("recall:{0:.3f}".format(recall))
    print("F1:{0:.3f}".format(F1))
