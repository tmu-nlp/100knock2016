import sys
import json

for line in open(sys.argv[1]):
    data=json.loads(line)
    if data["name"]==sys.argv[2]:
        print(data)
        break
