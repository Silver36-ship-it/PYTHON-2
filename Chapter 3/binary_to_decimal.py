binary = int(input("Enter 0's and 1's: "))
decimal = 0
position = 0		
while binary != 0:
	digit = binary % 10
	if digit not in (0,1):
		print("Invalid input")
		break 
	digit = binary % 10
	decimal += digit * (2**position)
	binary = binary // 10
	position = position + 1
else:
	print(decimal)




























