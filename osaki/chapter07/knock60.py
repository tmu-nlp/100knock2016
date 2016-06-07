import json
import plyvel
#import sys

area_db=plyvel.DB('/tmp/test.ldb',create_if_missing=True)
for line in open("artist.json","r"):
    data=json.loads(line)
    name=data["name"]
    if "area" in data:
        area=data["area"]
    else:
        area="NONE"
    area_db.put(name.encode('utf-8'),area.encode('utf-8'))

#print(area_db.get(sys.argv[1].encode('utf-8')))
area_db.close()
