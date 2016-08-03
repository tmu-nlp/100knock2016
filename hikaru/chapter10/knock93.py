def accuracy(file_name):
    total = 0
    count = 0
    for line in open(file_name):
        word1, word2, word3, word4, sim, value = line.strip('\n').split(' ')
        if word4 == sim:
            count += 1
        total += 1
    print (count / total * 100)

if __name__ == "__main__":
    accuracy('knock92_85.txt')
    accuracy('knock92_90.txt')
