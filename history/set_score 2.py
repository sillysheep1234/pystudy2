class Student():
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def get_score(self):
		return self.score

s=Student('black',99)

print(s.score)
s.get_score