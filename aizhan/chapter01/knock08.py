S = input('Enter string: ')

def cipher(some_s):
    sti = []
    ns = ''
    for c in some_s:
        nc = ord(c) 
        if not c.islower():
            sti.append(nc)
        else:
            sti.append(219 - nc)
    for n in sti:
        ns = ns + str(chr(n))
  
    return ns

ciphered = cipher(S)

print('暗号化:', ciphered)
print('復号化:', cipher(ciphered))

