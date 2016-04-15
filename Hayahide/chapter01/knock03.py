a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

ans = []

count = 0

for i in range(0, len(a)):
    if a[i] == " ":
        ans.append(str(count))
        count = 0

    elif a[i] != "," and a[i] != ".":
        count += 1

ans.append(str(count))
print ans
