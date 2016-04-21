s1 = 'パトカー'
s2 = 'タクシー'
answer = ''

for pair in zip(s1, s2):
    answer += pair[0] + pair[1]

print(answer)
