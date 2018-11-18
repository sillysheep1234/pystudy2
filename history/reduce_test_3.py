from functools import reduce
def chenfa(x,y):
	return x*y

result=reduce(chenfa,[1,2,3,4])
print('result=',result)