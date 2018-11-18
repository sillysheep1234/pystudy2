class Student():
	def __init__(self, name):
		self.name = name


	def __str__(self):
		return 'Student object (name: %s)' % self.name

a=Student('black')

print(a)
a
