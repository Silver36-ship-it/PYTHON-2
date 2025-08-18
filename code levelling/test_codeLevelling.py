import unittest
import function_codeLevelling

class TestCodeLevellingFunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_codeLevelling.add_number_to_tuple((1,22,32,23),4)
	def test_that_the_function_returns_true_value(self):
		result = function_codeLevelling.add_number_to_tuple((23,3,22,23,3),4)
		self.assertEqual(result,(23,3,22,23,3,4))
	def test_that_no_string_is_inputted(self):
		self.assertRaises(ValueError,function_codeLevelling.add_number_to_tuple,"weew",2)
	def test_that_no_strings_are_inputted_in_the_tuple(self):
		self.assertRaises(ValueError,function_codeLevelling.add_number_to_tuple,("weew","qqw"),2)
	def test_that_no_string_is_inputted_in_the_second_input(self):
		self.assertRaises(ValueError,function_codeLevelling.add_number_to_tuple,("wwq","ewww"),'wwqwq')
		
class TestThirdElementFunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_codeLevelling.change_the_element_value((1,2,[3,2],32),4)
	def test_that_the_function_returns_true_value(self):
		result = function_codeLevelling.change_the_element_value((1,2,[3,5],3),99)
		self.assertEqual(result,(1,2,[3,99],3))
	def test_that_no_string_is_inputted(self):
		self.assertRaises(ValueError,function_codeLevelling.change_the_element_value,"weew",2)
	def test_that_no_strings_are_inputted_in_the_tuple(self):
		self.assertRaises(ValueError,function_codeLevelling.change_the_element_value,("weew","qqw"),2)
	def test_that_no_string_is_inputted_in_the_second_input(self):
		self.assertRaises(ValueError,function_codeLevelling.change_the_element_value,("wwq","ewww"),'wwqwq')
		
class TestConversionToBothTupleAndStringFunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_codeLevelling.conversion_to_both_string_and_tuple(('apple','banana','cherry'),'mango')
	def test_that_the_function_returns_true_value(self):
		result = function_codeLevelling.conversion_to_both_string_and_tuple(('apple','banana','cherry'),'mango')
		self.assertEqual(result,('apple','banana','cherry','mango'))
	def test_that_no_integer_is_inputted(self):
		self.assertRaises(ValueError,function_codeLevelling.conversion_to_both_string_and_tuple,4,2)
	def test_that_no_integer_are_inputted_in_the_tuple(self):
		self.assertRaises(ValueError,function_codeLevelling.conversion_to_both_string_and_tuple,(32,43),2)
	def test_that_no_integer_is_inputted_in_the_second_input(self):
		self.assertRaises(ValueError,function_codeLevelling.conversion_to_both_string_and_tuple,(32,332),323)

class TestUnpackingTupleFunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_codeLevelling.unpack_tuple((3,2,2,5,4))
	def test_that_no_string_is_inputted(self):
		self.assertRaises(ValueError,function_codeLevelling.unpack_tuple,"weew")
	def test_that_no_strings_are_inputted_in_the_tuple(self):
		self.assertRaises(ValueError,function_codeLevelling.unpack_tuple,("weew","qqw"))
	def test_that_no_string_is_inputted_in_the_second_input(self):
		self.assertRaises(ValueError,function_codeLevelling.unpack_tuple,("wwq","ewww"))
	
class TestSumingUp2dListFunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_codeLevelling.sum_up_2d_list([[2,1,2],[21,2,2]])
	def test_that_the_function_returns_true_value(self):
		result = function_codeLevelling.sum_up_2d_list([[2,3,4],[1,5,7],[4,6,8]])
		self.assertEqual(result,[9,13,18])
	def test_that_no_string_is_inputted(self):
		self.assertRaises(ValueError,function_codeLevelling.sum_up_2d_list,"weew")
	def test_that_no_strings_are_inputted_in_the_list(self):
		self.assertRaises(ValueError,function_codeLevelling.sum_up_2d_list,[["weew","qqw"],["wqw","wqqw"]])	
	def test_that_no_strings_are_inputted_in_the_element(self):
		self.assertRaises(ValueError,function_codeLevelling.sum_up_2d_list,["weew","qqw"])		
	
class TestSumingUpCorrespondingIndexFunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_codeLevelling.sum_up_corresponding_index([[2,12,3],[3,32,2]])	
	def test_that_the_function_returns_true_value(self):
		result = function_codeLevelling.sum_up_corresponding_index([[2,3,4],[1,5,7],[4,6,8]])
		self.assertEqual(result,[7,14,19])
	def test_that_no_string_is_inputted(self):
		self.assertRaises(ValueError,function_codeLevelling.sum_up_corresponding_index,"weew")
	def test_that_no_strings_are_inputted_in_the_list(self):
		self.assertRaises(ValueError,function_codeLevelling.sum_up_corresponding_index,[["weew","qqw"],["wqw","wqqw"]])	
	def test_that_no_strings_are_inputted_in_the_element(self):
		self.assertRaises(ValueError,function_codeLevelling.sum_up_corresponding_index,["weew","qqw"])		
	
class TestMoreThanFiveCharactersFunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_codeLevelling.get_more_than_five_characters(['cat','dog','ewu'])
	def test_that_the_function_returns_true_value(self):
		result = function_codeLevelling.get_more_than_five_characters(['cat','elephant','tiger','lion'])
		self.assertEqual(result,['elephant','tiger'])
	def test_that_no_integer_is_inputted(self):
		self.assertRaises(ValueError,function_codeLevelling.get_more_than_five_characters,[4])
	def test_that_no_integer_are_inputted_in_the_tuple(self):
		self.assertRaises(ValueError,function_codeLevelling.get_more_than_five_characters,[32,43])
	def test_that_no_integer_is_inputted_in_the_second_input(self):
		self.assertRaises(ValueError,function_codeLevelling.get_more_than_five_characters,[3.2,332])
	def test_that_no_empty_string_is_inputted(self):
		self.assertRaises(ValueError,function_codeLevelling.get_more_than_five_characters,[""])

class TestFirstValueGreaterThanTwofunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_codeLevelling.list_of_tuples_more_than_two([(2,'A'),(2,'S')])	
	def test_that_the_function_returns_true_value(self):
		result = function_codeLevelling.list_of_tuples_more_than_two([(1,'A'),(4,'B'),(2,'C')])
		self.assertEqual(result,[(4,'B')])
	def test_that_no_empty_string_is_inputted(self):
		self.assertRaises(ValueError,function_codeLevelling.list_of_tuples_more_than_two,[""])

class TestPalindromeFunction(unittest.TestCase):
	def test_that_the_function_exist(self):
		function_codeLevelling.check_palindrome(['level','madam'])
	def test_that_the_function_returns_true_value(self):
		result = function_codeLevelling.check_palindrome(['level','world','madam','python'])	
		self.assertEqual(result,['level','madam'])	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		