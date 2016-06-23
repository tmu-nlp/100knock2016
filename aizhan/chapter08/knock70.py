import random

def data_shaping():
    sentiment = []
    count_pos = 0
    count_neg = 0
    for line in open('rt-polarity.pos', encoding='latin-1'):
        sentiment.append('+1 {}'.format(line))
        count_pos += 1
    for line in open('rt-polarity.neg', encoding='latin-1'):
        sentiment.append('-1 {}'.format(line))
        count_neg += 1

    random.shuffle(sentiment)

    with open('sentiment.txt', 'w') as f:
        for line in sentiment:
            f.write(line)
    print('pos:{}, neg:{}'.format(count_pos, count_neg))


if __name__ == '__main__':
    data_shaping()
