import sys
import json

for line in open(sys.argv[1]):
    data=json.loads(line)
    if "aliases" in data:
        for item in data["aliases"]:
            if item["name"]==sys.argv[2]:
                print(data["name"])
                break
