# knock62.py
# coding = utf-8

import sys, redis
r = redis.Redis(host="localhost", port=6379, db=0) 


for key in r.keys():
	if r.get(key).decode("utf-8") == "Japan":
		print (key.decode("utf-8"))