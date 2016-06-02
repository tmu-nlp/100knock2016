import re
cmpl = re.compile("[\.;:\?!] [A-Z]")

def make_sentence():
    ans_list = []
    for line in open("nlp.txt", "r"):
        line_list = cmpl.findall(line)
        if len(line_list) > 0:
            head = ""
            sentences = cmpl.split(line)
            for i in range(len(line_list)):
                mark = line_list[i].split()
                ans_list.append(head + sentences[i] + mark[0])
                head = mark[1]
            ans_list.append(head + sentences[-1])
    return ans_list

if __name__ == "__main__":
    nlp_list = make_sentence()
    for line in nlp_list:
        print (line)
