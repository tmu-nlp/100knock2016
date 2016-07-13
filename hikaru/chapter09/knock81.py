'''
f = open("country_list.txt", "w")
for country in open("countrylist.txt"):
    f.write(country.replace(" ", "_"))
f.close()
'''
clist = list()
for country in open("countrylist.txt"):
    clist.append(country)
c_list = list()
for country in open("country_list.txt"):
    c_list.append(country)
f = open("knock81.txt", "w")
for line in open("knock80.txt"):
    for c, c_ in zip(clist, c_list):
        if c in line:
            line = line.replace(c, c_)
    f.write(line)
f.close()