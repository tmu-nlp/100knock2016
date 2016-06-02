import plyvel

artist_DB = plyvel.DB("artist_DB.ldb", create_if_missing = False)
count = 0

for key, value in artist_DB:
    if value.decode() == "Japan":
        count += 1

print(count)

artist_DB.close()
