import sys
from nltk.corpus import stopwords

def stop(query):
    stop_list = stopwords.words('english')
    stop_list += ['.', ',', '(', ')', '?', '!', ':', ';']

    return True if query in stop_list else False

if __name__ == '__main__':
    query = sys.argv[1:]
    answer = []

    for word in query:
        if stop(word) == False:
            answer.append(word)
    print(' '.join(answer))
