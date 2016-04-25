#!/usr/bin/python
#_*_coding:utf-8_*_


def main():
    str_1 = "paraparaparadise"
    str_2 = "paragraph"
    X = list()
    Y = list()
    for i in range(len(str_1)):
        X.append(str_1[i:i+2])
    for i in range(len(str_2)):
        Y.append(str_2[i:i+2])
    X_set = set(X)
    Y_set = set(Y)
    print "和集合:"
    print list(X_set | Y_set)
    print "積集合:"
    print list(X_set & Y_set)
    print "差集合:"
    print list(X_set - Y_set)

    if "se" in list(X_set):
        print "X contains 'se'"
    else:
        print "X doesn't contain 'se'"
    if "se" in list(Y_set):
        print "Y contains 'se'"
    else:
        print "Y doesn't contain 'se'"



if __name__ == "__main__":
    main()

