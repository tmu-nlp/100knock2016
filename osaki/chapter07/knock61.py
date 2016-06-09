import plyvel
import sys

area_db=plyvel.DB('./arealdb/',create_if_missing=True)
print(area_db.get(sys.argv[1].encode('utf-8')))
