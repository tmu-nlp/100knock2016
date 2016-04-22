import re

s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
pi_list = []

for word in re.sub('[.,]', '', s).split(' '):
    pi_list.append(len(word))

print(pi_list)
    
