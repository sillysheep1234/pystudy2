try:
	r=10/0
	print(r)
except Exception as e:
	print('error',e)
finally:
	print('end')