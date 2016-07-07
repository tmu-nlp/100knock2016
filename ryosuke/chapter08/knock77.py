tp = 0
tn = 0
fp = 0
fn = 0
total = 0
for line in open('knock76.txt'):
    total += 1
    t, y, _ = line.split('\t')
    if t == y:
        if y == '1':
            tp += 1
        else:
            tn += 1
    else:
        if y == '1':
            fp += 1
        else:
            fn += 1

acc = (tp + tn) / total
pre = tp / (tp + fp)
rec = tp / (tp + fn)
f1 = 2 * rec * pre / (rec + pre)
print('正解率:{:.3f}, 適合率:{:.3f}, 再現率:{:.3f}, F1:{:.3f}'.format(acc, pre, rec, f1))
