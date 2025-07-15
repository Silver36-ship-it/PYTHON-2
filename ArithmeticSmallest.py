number = int(input('Enter an Integer:'))
number1 = int(input('Enter an Integer:'))
number2 = int(input('Enter an Integer:'))
sum = number + number1 + number2
average = sum / 3 
product = number * number1 * number2
smallest = number
largest = number 
print('Sum is',  sum)
print('Average is',  average)
println('product is',  product)
if smallest > number1: smallest = number1
if smallest > number3: smallest = number2
print('Smallest is:', smallest)
if largest < number1: largest = number1
if largest < number3: largest = number3
print('Largest is', largest)
