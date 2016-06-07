import plyvel


name2area_db = plyvel.DB('name2area_db.ldb')

c = 0
for name, area in name2area_db:
    if area == b'Japan':
        c += 1
print(c)
