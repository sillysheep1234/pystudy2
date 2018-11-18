class Fib(object):
	def __init__(self):
		self.a=0
		self.b=1
		self.mid=0
	def __iter__(self):
		return self
	def __next__(self):
		self.mid=self.a
		self.a=self.b
		self.b=self.mid+self.b
		if self.a>100000:
			raise StopIteration();
		return self.a

print(Fib())

for n in Fib():
	print(n)
