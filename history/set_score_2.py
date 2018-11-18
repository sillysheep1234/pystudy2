class Student():
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def get_score(self):
		return self.score

a=Student('black',99)

print(a.score)
print(a.get_score())