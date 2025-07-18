number = int(input('Enter number'))
separate = int(number / 10000)
separate2 = int(number / 1000) % 10
separate3 = int(number / 100) % 10
separate4 = int(number / 10) % 10
separate5 = int(number % 10)
print(separate, separate2, separate3, separate4, separate5)