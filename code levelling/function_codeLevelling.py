def add_number_to_tuple(tuple_of_numbers,number):
	if (type(tuple_of_numbers) == str) or type(number) == str:
		raise ValueError
	for value in tuple_of_numbers:
		if type(value) == str:
			raise ValueError
	return tuple_of_numbers + (number,)
	
def change_the_element_value(tuple_of_numbers,number):
	if (type(tuple_of_numbers) == str) or type(number) == str:
		raise ValueError
	for value in tuple_of_numbers:
		if type(value) == str:
			raise ValueError 
	tuple_of_numbers[2][1] = number
	return tuple_of_numbers
	
def conversion_to_both_string_and_tuple(tuple_of_strings,string):
	if (type(tuple_of_strings) == int) or type(string) == int:
		raise ValueError
	for value in tuple_of_strings:
		if type(value) == int:
			raise ValueError 
	new_list = []
	for strings in tuple_of_strings:
		new_list.append(strings)
	new_list.append(string)
	return tuple(new_list)
	
def unpack_tuple(tuple_of_numbers):
	if (type(tuple_of_numbers) == str):
		raise ValueError
	for value in tuple_of_numbers:
		if type(value) == str:
			raise ValueError 
	a,b,*others = tuple_of_numbers
	return a,b,*others	

def sum_up_2d_list(list_of_numbers):
	if (type(list_of_numbers) == str):
		raise ValueError
	new_list = []
	for element in range(0,len(list_of_numbers)):
		sum = 0
		for number in range(0,3):
			if type(list_of_numbers[element][number]) == str:
				raise ValueError
			sum = sum + list_of_numbers[element][number]
		new_list.append(sum)
	return new_list
	
def sum_up_corresponding_index(list_of_numbers):
	if (type(list_of_numbers) == str):
		raise ValueError
	new_list = []
	for element in range(0,len(list_of_numbers)):
		sum = 0
		for number in range(0,len(list_of_numbers)):
			if type(list_of_numbers[number][element]) == str:
				raise ValueError
			sum = sum + list_of_numbers[number][element]
		new_list.append(sum)
	return new_list

def even_number(x):
		return x % 2 == 0
def get_even_numbers():
	return list(filter(even_number,range(1,21)))
	
def list_of_words(x):
	if x == "":
		raise ValueError
	if(type(x) == int or type(x) == float):
		raise ValueError
	return len(x) >= 5
def get_more_than_five_characters(words):
	return list(filter(list_of_words,words))
	
def list_tuples(x):
	if x == "":
		raise ValueError
	index = 0
	return x[index] > 2
def list_of_tuples_more_than_two(list_of_tuples):
	return list(filter(list_tuples,list_of_tuples))
	 
def list_of_numbers(x):
	return x % 3 == 0 and x % 5 == 0
def get_divisible_by_both_numbers():
	return list(filter(list_of_numbers,range(1,51)))	

def palindrome_words(x):
	return x == x[::-1]	
def check_palindrome(words):
	return list(filter(palindrome_words,words))
	
def convert_uppercase(x):
	return x.upper()
def get_uppercase(words):
	return list(map(convert_uppercase,words))

def square_numbers(x):
	return x**2
def get_squared_numbers():
	return list(map(square_numbers,range(1,11)))

def first_letter_capitalization(x):
	index = 0
	return x[index].upper() + x[1:]
def get_first_letter_capitalization(words):
	return list(map(first_letter_capitalization,words))
	
def add_ten_percent(x):
	return 0.10 * x
def get_add_ten_percent(list_of_numbers):
	return list(map(add_ten_percent,list_of_numbers))

def sum_of_numbers(x,y):
	return x + y
def get_sum_of_numbers():
	return reduce(sum_of_numbers,range(1,51))





















