numbers = [1,2,3,4,5,6,7,8,9,10]
filtered_number = list(map(lambda x: x * 3,
         filter(lambda x: x % 2 == 0, numbers)))
print(sum(filtered_number))

list_check = [x * 3 for x in numbers if x % 2 == 0]
print(sum(list_check))