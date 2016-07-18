flag = False
w_file = open('knock91_result.txt', 'w')
for line in open('questions-words.txt'):
    words = line.strip('\n').split()
    if words[0] == ':' and words[1] == 'family':
        flag = True
    elif words[0] == ':' and words[1] != 'family':
        flag = False

    if flag:
        w_file.write(line)
w_file.close()
