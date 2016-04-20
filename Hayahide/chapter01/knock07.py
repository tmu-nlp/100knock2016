#-*- coding: utf-8 -*-

def template(x, y, z):
    return str(x) + "時の" + str(y) + "は" + str(z)

x, y, z = raw_input().split()

print template(x, y, z)
