# -*- coding: utf-8 -*-

def cipher(s):
    result = ""
    for i in range(len(s)):
        if ord(s[i]) >= ord("a") and ord(s[i]) <= ord("z"):
            result += chr(219 - ord(s[i]))
        else:
            result += s[i]
    return(result)

ans = cipher("abcdefghijklmnopqrstuvwxyz123456789ABCD")
print(ans)
print(cipher(ans))
