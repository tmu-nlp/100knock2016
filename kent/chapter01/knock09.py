#!/usr/bin/python
#_*_coding:utf-8_*_

import random

def main():
    source = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = source.strip().split(" ")
    new_str = list()
    for word in words:
        if len(word) > 4:
            shuffled_char = random.sample(list(word[1:-1]), len(list(word[1:-1])))
            new_str.append(word[:1] + "".join(shuffled_char) + word[-1:])
        else:
            new_str.append(word)
    print " ".join(new_str)


if __name__ == "__main__":
    main()

