def main():
    for line in open('./questions-words.txt', 'r'):
        if line.startswith(':'):
            section = line.strip('\n')
        elif section == ': family':
            print(line.strip('\n'))


if __name__ == '__main__':
    main()
