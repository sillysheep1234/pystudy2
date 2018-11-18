def is_palindrome(n):
	stringnum=str(n)
	return stringnum==stringnum[::-1]

output=filter(is_palindrome,range(1,1000))
print(list(output))

