total = 0
v85_true = 0
v90_true = 0

for line1, line2 in zip(open("result_92_v85.txt", "r"), open("result_92_v90.txt", "r")):
    total += 1
    if line1.strip().split()[3] == line1.strip().split()[4]:
        v85_true += 1
    if line2.strip().split()[3] == line2.strip().split()[4]:
        v90_true += 1

print("v85_accuracy：{}%".format(100 * v85_true / total))
print("v90_accuracy：{}%".format(100 * v90_true / total))
