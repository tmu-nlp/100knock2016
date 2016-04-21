#coding: utf-8

def cipher(text):
    answer = []
    for num,i in enumerate(text):
        if i.islower():
            answer.append(chr(219-ord(i)))
        else:
            answer.append(i)
    return "".join(answer)
            
text = raw_input()
print(cipher(text))
print(cipher(cipher(text)))
