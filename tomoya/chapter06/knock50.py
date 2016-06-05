import re


def getSentence():
    searchPause = re.compile("(?P<before>[\.;\:\?!]) (?P<after>[A-Z])")
    sentence = list()
    for line in open("nlp.txt"):
        sentence.append(searchPause.sub(r"\g<before>\n\n\g<after>", line))
    return sentence

if __name__ == "__main__":
    sentences = getSentence()
    for sentence in sentences:
        print(sentence)
