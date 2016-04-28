my_string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = my_string.split(" ")
# print (word_list)
my_dic = dict()
for i in range(len(word_list)):
	word = word_list[i]
	if i + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
		my_dic[word[0]] = i + 1
	else:
		my_dic[word[0:2]] = i + 1
	print ("%d:%s" % (i, word))



	# print (word)
	# if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
	# 	print (i, word[0])
	# else:
	# 	print(i ,word[0:2])
print (my_dic)

# print (len(my_dic))
