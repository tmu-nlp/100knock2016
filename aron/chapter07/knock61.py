# knock61.py
# coding = utf-8
import sys, redis
r = redis.Redis(host="localhost", port=6379, db=0) 

while(True):
	line = input(" # Artist name >> ")
	if(line == "exit"):
		print ("Bye bye")
		break
	else:
		print(r.get(line).decode("utf-8"))
		# print (str(r.get(line)))
