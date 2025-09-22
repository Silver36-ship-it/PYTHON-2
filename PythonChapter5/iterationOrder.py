row = 2
column = 3
number_list = []
counter = 1
for _ in range(row):
    row = []
    for _ in range(column):
        row.append(counter)
        counter += 1
    number_list.append(row)
print("     ",end="")
for index, row in enumerate(row):
    print(f"{index:^5}",end="")
print("\n" + "=" * 28)

for index, row in enumerate(number_list):
    print(f"{index:^4}|",end="")
    for value in row:
        print(f"{value:^5}",end="")
    print()
