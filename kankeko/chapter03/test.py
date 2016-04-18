import re


text = "[[bcdefghaij"

print(re.sub("\[.+","aaaaaa",text))
