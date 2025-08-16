def square_number(number):
	if number == "":
		raise ValueError
	if(type(number) == str):
		raise ValueError
	if(type(number) == 0):
		raise ValueError
	if number < 0:
		raise ValueError
	return number ** 2
def list_of_numbers(number_list):
	return list(map(square_number,number_list))
	
def strings_length(strings_input):
	if strings_input == "":
		raise ValueError
	if(type(strings_input) == int):
		raise ValueError
	if (type(strings_input) == float):
		raise ValueError
	return len(strings_input)
def length_of_string(strings):
	return list(map(strings_length,strings))
	
def even_number(x):
	if x == "":
		raise ValueError
	if(type(x) == str):
		raise ValueError
	if x < 0:
		raise ValueError
	return x % 2 == 0
def list_of_even_numbers(numbers):
	return list(filter(even_number,numbers))
	
def list_of_strings(x):
	if x == "":
		raise ValueError
	if(type(x) != str):
		raise ValueError
	return len(x) >= 5
def string_more_than_five_characters(strings):
	return list(filter(list_of_strings,strings))
	
