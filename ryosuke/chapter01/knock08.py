def cipher(s):
    news = ''
    for t in s:
        if 97 <= ord(t) and ord(t) <= 122:
            t = chr(219 - ord(t))
        news += t
    return news

s = 'hogeHoGE'
print(s)
print(cipher(s))
print(cipher(cipher(s)))
