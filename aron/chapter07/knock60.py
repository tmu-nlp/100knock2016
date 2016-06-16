# knock60.py
# coding = utf-8

import sys, json
import redis

r = redis.Redis(host="localhost", port=6379, db=0) 

with open("artist.json", "r") as file:
	for line in file:
		# dic = defaultdict(lambda : 0)
		dic = json.loads(line.rstrip())
		if "name" in dic.keys() and "area" in dic.keys():
			name = dic["name"]
			area = dic["area"]
			r.set(name.encode('utf-8'), area.encode('utf-8'))

