number = int(input('Enter number:'))
if number < 0:
	print("Invalid input")
else:
	factorial = 1
	for count in range(1,number + 1):
		factorial *= count
	print(factorial)