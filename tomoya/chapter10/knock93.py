def main():
    num = 0
    correct_92 = 0
    correct_85 = 0
    for line1, line2 in zip(open('knock85.data', 'r'), open('knock92.data', 'r')):
        analogy1 = line1.split(' ')
        analogy2 = line2.split(' ')
        num += 1
        if analogy1[3] == analogy1[4]:
            correct_85 += 1
        if analogy2[3] == analogy2[4]:
            correct_92 += 1
        print('knock85 正解率: {}'.format(correct_85 / num))
        print('knock92 正解率: {}'.format(correct_92 / num))

if __name__ == '__main__':
    main()
