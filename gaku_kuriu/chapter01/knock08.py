def cipher(s):
    answer = ''
    for w in s:
        if ord('a') <= ord(w) and ord(w) <= ord('z'):
            answer += chr(219 - ord(w))
        else:
            answer += w
    return(answer)

s = 'Hello World!'
print('default:', s)
print('encoded:', cipher(s))
print('decoded:', cipher(cipher(s)))


