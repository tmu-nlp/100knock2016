import re

country_list = list()
for country in open('country-name.txt', 'r'):
  country_list.append(country.strip('\n'))

for line in open('./enwiki-corpus.txt', 'r'):
  line.strip('\n')
  for country in country_list:
    line = line.replace(country, country.replace(' ', '_'))
  print(line, end='')
