accumulated_miles = 0
accumulated_gallons = 0
while True:
	miles_driven = float(input('Enter miles(press -1 to end):'))
	if miles_driven == -1:
		break
	gallons_used = float(input('Enter gallons'))
	accumulated_miles += miles_driven
	accumulated_gallons += gallons_used
	miles_per_gallon = miles_driven / gallons_used
	print(f'{miles_per_gallon:.2f}')
if accumulated_gallons > 0:
	average = accumulated_miles / accumulated_gallons
	print(f'Overall average miles/gallon used is {average:.2f}')
else:
	print('invalid input')