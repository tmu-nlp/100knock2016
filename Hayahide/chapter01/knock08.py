def cipher(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i].islower():
            s_list[i] = chr(219 - ord(s_list[i]))

    return "".join(s_list)

s = raw_input()
s_cipher = cipher(s)
print "cipher: " + s_cipher
print "decode: " + cipher(s_cipher)
