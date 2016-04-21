#-*- coding:utf-8 -*-

#「パタトクカシーー」
#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．


cars = u"パタトクカシーー"

# # made an empty list to put characters later
# word1 = []
#
# # made a loop. gave 0,2,4,6.
# for i in range(0,7,2):
#
#     # append パ,ト,カ,ー to word1.
#     word1.append(cars[i])
# # join パ,ト,カ,ー in a string.
# car = ''.join(word1)
#
# print(car)


#def my_function(my_argument):
def print_extracted_car(hajime, owari):
    word1 = []

    # made a loop. gave 1,3,5,7.
    for i in range(hajime,owari,2):

        # append タ,ク,シ,ー to word1.
        word1.append(cars[i])
    # join タ,ク,シ,ー in a string.
    car = ''.join(word1)

    print(car)

print_extracted_car(1,8)
print_extracted_car(0,7)

# defmain(word):
    # print "".join(list(word)[::2]).encode("utf-8")

# if __name__ == '__main__':
    # main(u"パタトクカシーー")

