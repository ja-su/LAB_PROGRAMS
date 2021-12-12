import pickle
dict = {'one': 1,'Two': 2}
file = open('dump.txt','wb')
pickle.dump(dict,file)
file.close()
