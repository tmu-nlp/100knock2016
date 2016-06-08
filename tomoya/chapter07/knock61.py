import plyvel
import sys

my_db = plyvel.DB('test.ldb')
print(my_db.get(sys.argv[1].encode('utf-8')))
my_db.close()
