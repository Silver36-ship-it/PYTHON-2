import unittest
import function_taskOne

class TestSquaresOfNumberFunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_taskOne.list_of_numbers([2,3,13])	
	def test_that_numbers_are_squared_up(self):
		result = function_taskOne.list_of_numbers([3,2,4,5])
		self.assertEqual(result,[9,4,16,25])
	def test_that_number_doesnt_return_string(self):
		self.assertRaises(ValueError,function_taskOne.list_of_numbers, "string")	
	def test_that_no_empty_string_is_inputted(self):
		self.assertRaises(ValueError,function_taskOne.list_of_numbers, [""])	
	def test_that_input_is_not_less_than_zero(self):
		self.assertRaises(ValueError,function_taskOne.list_of_numbers, [-2,-22,-4])
		
class TestLengthOfStringsFunction(unittest.TestCase):
	def test_that_the_function_exists(self):
		function_taskOne.length_of_string(['apple','eewqe','wwqw'])
	def test_that_the_input_returns_length(self):
		result = function_taskOne.length_of_string(['wew','weeee','wewq'])
		self.assertEqual(result,[3,5,4])
	def test_that_the_input_is_not_an_integer(self):
		self.assertRaises(ValueError,function_taskOne.length_of_string, [33,22,22])
	def test_that_the_input_is_an_empty_string(self):
		self.assertRaises(ValueError,function_taskOne.length_of_string, [""])
	def test_that_the_input_is_not_negative_float_type(self):
		self.assertRaises(ValueError,function_taskOne.length_of_string,[-3.33,-3.3])

class TestEvenNumbersFunction(unittest.TestCase):
	def test_that_the_function_exists(self):
		function_taskOne.list_of_even_numbers([32,32,323])
	def test_that_the_function_returns_even_numbers(self):
		result = function_taskOne.list_of_even_numbers([2,23,3,223,3,32,3])
		self.assertEqual(result,[2,32])
	def test_that_the_input_is_not_an_integer(self):
		self.assertRaises(ValueError,function_taskOne.list_of_even_numbers, "jj")
	def test_that_the_input_is_not_an_empty_input(self):
		self.assertRaises(ValueError,function_taskOne.list_of_even_numbers, [""])
	def test_that_the_input_is_not_a_negative_input(self):
		self.assertRaises(ValueError,function_taskOne.list_of_even_numbers,[-3,-32,-43])
		
class TestListOfStringsFunction(unittest.TestCase):
	def test_that_the_function_exists(self):
		function_taskOne.string_more_than_five_characters(['hi','hello','wadup','sup'])
	def test_that_the_function_returns_more_than_five_characters(self):
		result = function_taskOne.string_more_than_five_characters(['lambo','aeroplane','porche','boy','luxury','fish'])
		self.assertEqual(result,['lambo','aeroplane','porche','luxury'])
	def test_that_no_empty_string_is_inputted(self):
		self.assertRaises(ValueError,function_taskOne.string_more_than_five_characters,[""])
	def test_that_no_integer_is_inputted(self):
		self.assertRaises(ValueError,function_taskOne.string_more_than_five_characters,[32,3,22,3])
	def test_that_no_negative_integer_is_inputted(self):
		self.assertRaises(ValueError,function_taskOne.string_more_than_five_characters,[-22.2,-211,11,-3])