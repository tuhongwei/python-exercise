#three methods
#first
def is_palindrome(n):
	return str(n)==str(n)[::-1]
output = filter(is_palindrome,range(1,1000))
print(list(output))

#second
def is_palindrome(n):
	chars = str(n)
	for i in range(0,len(chars)//2+1):
		if chars[i]!=chars[len(chars)-1-i]:
			return False
	return True
output = filter(is_palindrome2,range(1,1000))
print(list(output))

#three
def is_palindrome(n):
	m,i = 0,n
	while i:
		m = m*10 + i%10
		i = i//10
	if(m==n):
		return True
	else:
		return False
output = filter(is_palindrome,range(1,1000))
print(list(output))