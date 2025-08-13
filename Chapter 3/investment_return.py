amount_invested = int(input('Enter principal amount'))
annual_rate = float(input('Enter annual rate'))
for year in range(1,31):
	annual_deposit = amount_invested * (1 + annual_rate)**year
	print(f'{annual_deposit:.2f}')
	