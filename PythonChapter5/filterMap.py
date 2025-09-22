numbers = [3,4,5,4,2,2,10,7,8,9,9,8]
set_number = set(numbers)
result = list(map(lambda x: x ** 2,
                filter(lambda x: x % 2 != 0, set_number)))
print(result)