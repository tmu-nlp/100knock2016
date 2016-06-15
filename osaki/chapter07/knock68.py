import sys
import json

d={}
for line in open(sys.argv[1]):
    data=json.loads(line)
    if "tags" in data and "rating" in data:
        for item in data["tags"]:
            if item["value"]=="dance":
                d[data["name"]]=data["rating"]["count"]

c=0
for key,value in sorted(d.items(),key=lambda x:x[1],reverse=True):
    c+=1
    print(str(key)+"\t"+str(value))
    if c==10:
        break
