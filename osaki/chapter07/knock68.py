from pymongo import MongoClient

client=MongoClient()
db=client.artist_db
collection=db.artist_collection

d={}
for item in collection.find({"tags.value":"dance"}):
    if "rating" in item:
        d[item["name"]]=item["rating"]["count"]

c=0
for key,value in sorted(d.items(),key=lambda x:x[1],reverse=True):
    c+=1
    print(str(key)+"\t"+str(value))
    if c==10:
        break
