import pickle
f=open('dump2.txt','rb')
d=pickle.load(f)
f.close()
print(d)
