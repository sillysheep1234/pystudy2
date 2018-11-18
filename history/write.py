

#b=open('/test2.txt','r')
#print(b.read())

with open('/test3.txt', 'w') as f:
    f.write('Hello, world!')

a=open('/test3.txt','r')
print(a.read())
a.close()

