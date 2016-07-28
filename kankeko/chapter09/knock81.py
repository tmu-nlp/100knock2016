import re

countries = []
for country in open('list_of_countries.txt'):
    countries = country.split("\n")

for line in (open('corpus.txt')):
    for country in countries:
        if country in line:
            line = re.sub(country, country.replace(' ', '_'), line)
    print(line, end='')
