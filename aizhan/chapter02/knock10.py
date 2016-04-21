def gyousuu():
    count = 0
    for line in open('hightemp.txt'):
        count += 1
    print('行数のカウントは:', count)

gyousuu()
