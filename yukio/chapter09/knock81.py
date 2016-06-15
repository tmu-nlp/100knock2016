countries = []

for line in open("countries.txt", "r"):
    countries.append(line)

f = open("tokens_81.txt", "w")
for line in open("tokens_80.txt", "r"):
    for country in countries:
        line = line.replace(country, country.replace(" ", "_"))
    f.write(line)
    
f.close()
