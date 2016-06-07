import plyvel

area_db=plyvel.DB('/tmp/test.ldb',create_if_missing=True)

c=0
for key,value in area_db:
    if value==b'Japan':
        c+=1
print(c)
