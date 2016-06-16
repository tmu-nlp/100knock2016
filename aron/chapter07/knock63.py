# knock63.py
# coding = utf-8

import sys, json
import redis

r = redis.Redis(host="localhost", port=6379, db=1) 

with open("artist.json", "r") as file:
	for line in file:
		# dic = defaultdict(lambda : 0)
		dic = json.loads(line.rstrip())
		if "name" in dic.keys() and "tags" in dic.keys():
			name = dic["name"]
			tags = dic["tags"]
			# print(name)
			for tag in tags:
				# print("\t", tag["count"], tag["value"])
				r.hset(name.encode('utf-8'), tag["value"].encode('utf-8'), int(tag["count"]))

# r.set(name.encode('utf-8'), tags.encode('utf-8'))

# hgetall