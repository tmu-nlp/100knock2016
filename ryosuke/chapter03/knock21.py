from knock20 import getUKtext


for line in getUKtext().split('\n'):
    if 'Category' in line:
        print(line)
