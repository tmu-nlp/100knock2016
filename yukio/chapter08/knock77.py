def calc_score(result):
    total_count = 0
    correct_count = 0
    pos_cor_count = 0
    pos_ans_count = 0
    pos_pre_count = 0

    for ans, pre in result:
        if ans == pre:
            correct_count += 1
            if ans == "1":
                pos_cor_count += 1
        total_count += 1
        if ans == "1":
            pos_ans_count += 1
        if pre == "1":
            pos_pre_count += 1
    
    accuracy = correct_count / total_count
    if pos_pre_count != 0:
        precision = pos_cor_count / pos_pre_count
    else:
        precision = 1.0
    recall = pos_cor_count / pos_ans_count
    f1score = 2 * precision * recall / (precision + recall)

    return accuracy, precision, recall, f1score

if __name__ == "__main__":
    from knock76 import result
    for line in result:
        del line[2]
    accuracy, precision, recall, f1score = calc_score(result)
    print("Accuracy:{}%".format(100 * accuracy))
    print("Precision:{}%".format(100 * precision))
    print("Recall:{}%".format(100 * recall))
    print("F1-Score:{}%".format(100 * f1score))
