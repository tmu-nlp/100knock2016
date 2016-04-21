s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

key = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}
elem = ""

count = 1
key_count = 0

for i in range(len(s)):
    if s[i] == " ":
        if key[key_count] == count:
            dict[elem[0]] = count
            key_count += 1

        else:
            dict[elem[:2]] = count
        
        elem = ""
        count += 1

    else:
        elem = elem + s[i]

print dict

