# -*- coding: utf-8 -*-


#「パトカー」＋「タクシー」＝「パタトクカシーー」
#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

# made lists "パ,ト,カ,ー" and "タ,ク,シ,ー"
car1 = list(u"パトカー")
car2 = list(u"タクシー")

# made an empty list to put characters later
cars = []

# made a loop, gave 0,1,2,3 for each list (car1 and car2)
for i in range(4):
    # Take the first character "パ" from car1 and "タ" from car2.
    # then put these into a list. repeat this until the end.
    cars.append(car1[i])
    cars.append(car2[i])

# joined list of characters into string.
cars2 = ''.join(cars)

# print result.
print(cars2)

# def main(word1, word2):
    #print "".join([char1 + char2 for char1, char2 in zip(word1, word2)]).encode("utf-8")

# if __name__ == '__main__':
#    main(u"", u"")
