import sys


def similarity_check(f):
    count = 0
    line_count = 0
    none_count = 0
    for line in open(f, 'r'):
        line_count += 1
        words = line.strip('\n').split()
        if words[4] == '<None>':
            none_count += 1
        elif words[3] == words[4]:    
            count += 1
    return count, line_count, none_count

if __name__ == '__main__':
    files = sys.argv[1:]
    for f in files:
        count, line_count, none_count = similarity_check(f)
        print('Accuracy: {}'.format(count / line_count))
        print('Accuracy (except None): {}'.format(count / (line_count - none_count)))
