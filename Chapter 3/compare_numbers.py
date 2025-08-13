print('Enter two numbers to compare')
number = int(input('Enter number'))
number1 = int(input('Enter another number'))
if number == number1:
	print('Both numbers are equal')
else:
	print('Not equal')
if number < number1:
	print(number, 'is less than', number1)
else:
	print(number, 'is greater than or equal to', number1)
if number <= number1:
	print(number, 'is less than or equal to', number1)
