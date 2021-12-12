import pickle
file=open('dump.txt','rb')
dict=pickle.load(file)
file.close()
