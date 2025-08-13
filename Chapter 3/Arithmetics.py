number = int(input('Enter a number'))
sum = number
product = number
smallest = number
largest = number
for count in range(1,4):
	number1 = int(input('Enter a number'))
	if number1 > largest:
		largest = number1
	if number1 < smallest:
		smallest = number1 
	sum += number1   
	product *= number1
	average = sum/4
print('Sum is ',sum)
print('Product is ',  product)
print('Average is ', average)
print('Largest is ', largest)
print('Smallest is ', smallest)