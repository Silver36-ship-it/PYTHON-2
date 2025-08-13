number = int(input('Enter number: '))
seperator = 10000
for count in range(5):
	digit = number // seperator
	print(digit,end =' ')
	number = number % seperator
	seperator //= 10
		