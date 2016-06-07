import json
import plyvel

area_db=plyvel.DB('./arealdb/',create_if_missing=True)
for line in open("artist.json","r"):
    data=json.loads(line)
    name=data["name"]
    if "area" in data:
        area=data["area"]
    else:
        area="NONE"
    area_db.put(name.encode('utf-8'),area.encode('utf-8'))

area_db.close()
