import sys
import plyvel


name2area_db = plyvel.DB('name2area_db.ldb')
for name in iter(sys.stdin.readline, '\n'):
    name = name.rstrip('\n').encode('utf-8')
    area = name2area_db.get(name)
    if area is not None:
        area = area.decode('utf-8')
    print(area)
    print()
