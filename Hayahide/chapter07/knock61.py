import plyvel
import sys

artist_db = plyvel.DB('artist_db.ldb', create_if_missing=False)
query = ' '.join(sys.argv[1:])

artist_area = artist_db.get(query.encode('utf-8'))
if artist_area:
    print(artist_area.decode())
else:
    print("'" + query + "' does not exist in this database.")
