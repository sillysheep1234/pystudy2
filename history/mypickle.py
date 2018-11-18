import pickle
d=dict(name='Bob',age=20,score=88)
f=open('dump3.txt','w')
pickle.dump(d,f)
f.close()
g=open('dump3.txt','r')
print(g.read())
