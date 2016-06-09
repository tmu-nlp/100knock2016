import gzip
import json
import plyvel

my_db = plyvel.DB('plyveldb', create_if_missing=True)  # なければつくる
for line in gzip.open("artist.json.gz"):
    my_dict = json.loads(line.decode('utf-8'))
    name = my_dict['name']
    area = my_dict['area'] if 'area' in my_dict.keys() else '不明'
    my_db.put(name.encode('utf-8'), area.encode('utf-8'))
    #my_db.put(name, area) #できないよ
print (my_db.get('Oasis'.encode('utf-8')))
my_db.close()


