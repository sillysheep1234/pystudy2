import re
test='010 12345'

if re.match(r'^\d{3}-\d{3,8}$',test):
	print('ok')
else:
	print('failed')