integer = int(input('Enter Integer'))
if integer < 10000 or integer > 99999:
	print("Inavlid input,put five digits")
else:
	digit1 = integer // 10000
	digit2 = (integer // 1000) % 10
	digit3 = (integer // 100) % 10
	digit4 = (integer // 10) % 10
	digit5 = integer % 10
	if digit1 == digit5 and digit2 == digit4:
		print("Number is a palindrome")
	else:
		print("Not a palindrome")