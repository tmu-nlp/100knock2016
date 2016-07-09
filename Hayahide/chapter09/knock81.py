#country list:
#http://zxcvbnmnbvcxz.com/%E8%8B%B1%E8%AA%9E%E8%A1%A8%E8%A8%98-%E5%9B%BD%E5%90%8D%E4%B8%80%E8%A6%A7-select-option%E7%AD%89%E3%81%A7%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E6%99%82%E3%81%AE%E7%82%BA%E3%81%AB/

country = dict()
for line in open('country.txt', 'r'):
    line = line.strip('\n')
    country[line] = line.replace(' ', '_')

w_file = open('knock81_corpus.txt', 'w')
for line in open('knock80_corpus.txt', 'r'):
    for before, after in country.items():
        if before in line:
            line = line.replace(before, after)
    w_file.write(line)
w_file.close()
