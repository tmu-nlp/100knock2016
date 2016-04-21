s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans = []
s = s.replace(",", "")
s = s.replace(".", "")
words = s.split()
for word in words:
    ans.append(len(word))
print(ans)
