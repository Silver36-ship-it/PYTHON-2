print(f'{"number":>5} {"Square":>5} {"Cube":>5}')
for i in range(6):
	square = i ** 2
	cube = i ** 3
	print(f'{i:>5} {square:>5} {cube:>5}')
