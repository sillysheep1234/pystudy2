L1=[('Lili',75),('Adam',92),('Bart',66),('Lisa',68)]

def name(x):
	i=0	
	L2=[]
	while i<len(x):
		L2.append(L1[i][0])
		i=i+1
	return L2

output=sorted(L1,key=name)
print(output)