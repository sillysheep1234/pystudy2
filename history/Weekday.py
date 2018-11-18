from enum import Enum,unique

@unique
class Weekday(Enum):
	Sun=0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6

#print(Weekday.Mon)
#print(Weekday.Mon.value)
#print(Weekday(1))

for a,b in Weekday.__members__.items():
    print(a, '=>', b,b.value)

#for name, member in Weekday.members.items():
#    print(name, '=>', member)