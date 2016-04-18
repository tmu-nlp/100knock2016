# -*- coding: utf-8 -*-

# 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# open a file named 'hightemp.txt' as variable file.
file_to_be_counted = open('hightemp.txt')
# the number of lines
line_count = 0
# in every line in file_to_be_counted...
for line in file_to_be_counted:
    # +1 to line_count in file_to_be_counted
    line_count += 1
print line_count
