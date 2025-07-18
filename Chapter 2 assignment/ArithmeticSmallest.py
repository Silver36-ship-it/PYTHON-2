number = int(input('Enter an Integer:'))
number1 = int(input('Enter an Integer:'))
number2 = int(input('Enter an Integer:'))
sum = number + number1 + number2
average = int(sum / 3)
product = number * number1 * number2
smallest = number
largest = number 
print('Sum is',  sum)
print ('Average is', average)
print('product is',  product)
if smallest > number1: smallest = number1
if smallest > number2: smallest = number2
print('Smallest is:', smallest)
if largest < number1: largest = number1
if largest < number2: largest = number2
print('Largest is', largest)
