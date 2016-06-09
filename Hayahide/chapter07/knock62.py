import plyvel

artist_db = plyvel.DB('artist_db.ldb', create_if_missing=False)

count = 0
for key, value in artist_db:
    if value.decode() == 'Japan':
        count += 1
print(count)

artist_db.close()
