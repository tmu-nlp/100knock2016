# cut -c1 sentiment.txt | sort | uniq -c
import random


def main():
    sentiment = list()
    for line in open('rt-polarity.pos'):
        sentiment.append('+1 ' + line)
    for line in open('rt-polarity.neg'):
        sentiment.append('-1 ' + line)
    random.shuffle(sentiment)
    with open('sentiment.txt', 'w') as fp:
        print(''.join(sentiment), file=fp, end="")

if __name__ == '__main__':
    main()
