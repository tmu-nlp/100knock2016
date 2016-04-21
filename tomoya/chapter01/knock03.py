s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(",", "").replace(".", "")
t = s.split(" ")
t = [len(x) for x in t]
print(t)