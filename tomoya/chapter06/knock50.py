import re


def getSentence():
    searchPause = re.compile("(?P<before>.*?[\.;\:\?!])\s(?P<after>[A-Z].*?)")
    sentence = list()
    for line in open("nlp.txt"):
        sentence.append(searchPause.sub(r"\g<before>\n\g<after>", line).strip("\n"))
    return sentence

if __name__ == "__main__":
    sentences = getSentence()
    for sentence in sentences:
        print(sentence)
