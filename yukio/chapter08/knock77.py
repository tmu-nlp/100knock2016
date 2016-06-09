from knock76 import result

total_count = 0
correct_count = 0
pos_cor_count = 0
pos_ans_count = 0
pos_pre_count = 0

for line in result.split("\n"):
    ans, pre = line.split()[:2]
    if ans == pre:
        correct_count += 1
        if ans == 1:
            pos_cor_count += 1
    total_count += 1
    if ans == 1:
        pos_ans_count += 1
    if pre == 1:
        pos_pre_count += 1
        
precision = pos_cor_count / pos_pre_count
recall = pos_cor_count / pos_ans_count

print("Accuracy:{}%".format(100 * correct_count / total_count))
print("Precision:{}%".format(100 * precision))
print("Recall:{}%".format(100 * recall))
print("F1-Score:{}".format(2 * precision * recall / (precision + recall)))
