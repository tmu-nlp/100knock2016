import plyvel
my_db = plyvel.DB('test.ldb')
count = 0
for keydata, area in my_db:
    print(area)
    if area == b'Japan':
        count += 1
print(count)
my_db.close()
