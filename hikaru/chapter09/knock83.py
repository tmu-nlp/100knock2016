from collections import defaultdict

tc_dict = defaultdict(int)
t_dict = defaultdict(int)
c_dict = defaultdict(int)
total = 0

for line in open('knock82.txt'):
    line = line.strip('\n')
    tc_dict[line] += 1
    t, c = line.split('\t')
    #print ('{} {}'.format(t, c))
    t_dict[t] += 1
    c_dict[c] += 1
    total += 1

f1 = open('f_tc.txt', 'w')
f2 = open('f_t.txt', 'w')
f3 = open('f_c.txt', 'w')

for key, value in sorted(tc_dict.items(), key=lambda x: -x[1]):
    f1.write('{} {}\n'.format(key, value))
for key, value in sorted(t_dict.items(), key=lambda x: -x[1]):
    f2.write('{} {}\n'.format(key, value))
for key, value in sorted(c_dict.items(), key=lambda x: -x[1]):
    f3.write('{} {}\n'.format(key, value))
print (total)
f1.close()
f2.close()
f3.close()
