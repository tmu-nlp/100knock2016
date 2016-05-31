import plyvel
import sys

artist_DB = plyvel.DB("artist_DB.ldb", create_if_missing = False)

if artist_DB.get(str(sys.argv[1]).encode("utf-8")):
    print(artist_DB.get(str(sys.argv[1]).encode("utf-8")).decode())
else:
    print("{} does not exist".format(str(sys.argv[1])))

artist_DB.close()
