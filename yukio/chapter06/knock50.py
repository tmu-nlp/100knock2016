import re

def sentence_punc():
    ans = ""
    pattern = re.compile("(?P<last>[\.;:\?!]) (?P<first>[A-Z])")
    
    for line in open("nlp.txt", "r"):
        ans += re.sub(pattern, "\g<last>\n\g<first>", line)

    return ans

if __name__ == "__main__":
    print(sentence_punc())
        
    
