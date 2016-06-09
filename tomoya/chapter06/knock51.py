from knock50 import getSentence


def getWords():
    words = []
    for sentence in getSentence():
        words.extend(sentence.split(" "))
    return words

if __name__ == "__main__":
    words = getWords()
    for word in words:
        print(word.strip(",").strip("."))
