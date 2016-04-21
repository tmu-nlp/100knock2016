def n_gram(s, n):
    ans = [] 
    for i in range(0, len(s) - n + 1):
        gram = ""
        for j in range(i, i + n - 1):
            gram += s[j]
            gram += "-"
        gram += s[i + n - 1]
        ans.append(gram)
    return(ans)

X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))

print("集合X：{}".format(X))
print("集合Y：{}".format(Y))
print("和集合：{}".format(X | Y))
print("積集合：{}".format(X & Y))
print("差集合(X - Y)：{}".format(X - Y))
print("差集合(Y - X)：{}".format(Y - X))

if "s-e" in X & Y:
    print("bi-gram's-e'は集合XにもYにも含まれています")
elif "s-e" in X - Y:
    print("bi-gram's-e'は集合Xにのみ含まれています")
elif "s-e" in Y - X:
    print("bi-gram's-e'は集合Yにのみ含まれています")
else:
    print("bi-gram's-e'は集合XにもYにも含まれていません")
