from gensim.models import word2vec
import pickle

#関数つくらないで２つ分同じのまわしてるよ
f_90 = open("knock92_90.txt", "w")
model = word2vec.Word2Vec.load("knock90_word2vec")
unk_list = list()
f91 = open("knock91.txt")
for line in f91:
    word1, word2, word3, word4 = line.strip('\n').split(' ')
    if word1 in model and word2 in model and word3 in model:
        top = model.most_similar(positive=[word2, word3], negative=[word1], topn=1)
        #print ('{} {}'.format(top[0][0], top[0][1]))
        f_90.write('{} {} {} {} {} {}\n'.format(word1, word2, word3, word4, top[0][0], top[0][1]))
    else:
        f_90.write('{} {} {} {} unk 0\n'.format(word1, word2, word3, word4))
        if word1 not in model:
            unk_list.append(word1)
        if word2 not in model:
            unk_list.append(word2)
        if word3 not in model:
            unk_list.append(word3)
f91.close()
f_90.close()

f_85 = open("knock92_85.txt", "w")
model_85 = pickle.load(open('X_dict.pickle', mode='rb'))
unk_list_85 = list()
f91 = open("knock91.txt")
for line in f91:
    word1, word2, word3, word4 = line.strip('\n').split(' ')
    if word1 in model_85 and word2 in model_85 and word3 in model_85:
        top = model.most_similar(positive=[word2, word3], negative=[word1], topn=1)
        #print ('{} {}'.format(top[0][0], top[0][1]))
        f_85.write('{} {} {} {} {} {}\n'.format(word1, word2, word3, word4, top[0][0], top[0][1]))
    else:
        f_85.write('{} {} {} {} unk 0\n'.format(word1, word2, word3, word4))
        if word1 not in model_85:
            unk_list_85.append(word1)
        if word2 not in model_85:
            unk_list_85.append(word2)
        if word3 not in model_85:
            unk_list_85.append(word3)

print (set(unk_list_85))
print (set(unk_list))
f_85.close()
