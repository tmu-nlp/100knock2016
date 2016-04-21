s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ans = {}
i = 1
s = s.replace(",", "")
s = s.replace(".", "")
words = s.split()

for word in words:
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        ans[word[0]] = i
    else:
        ans[word[0:2]] = i
    i += 1
print(ans)
