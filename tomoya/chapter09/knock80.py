def main():
  for line in open('enwiki-20150112-400-r100-10576.txt', 'r'):
    words = line.strip('\n').split()
    word_list = list()
    for word in words:
      word = word.strip('.,!?;:()[]\'"')
      if word != "":
        word_list.append(word)
    print(" ".join(word_list))

if __name__ == '__main__':
  main()
