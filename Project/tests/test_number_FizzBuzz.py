from coe_number.number_FizzBuzz import get_Fizz_Buzz
import unittest


class FizzBuzzListTest(unittest.TestCase):
    def test_give_1_is_emtpy_str(self):
        number = 1
        is_fizzbuzz = get_Fizz_Buzz(number)
        self.assertEqual(is_fizzbuzz,"")
    
    # def test_give_5_is_buzz(self):
    #     number = 5
    #     is_fizzbuzz = get_Fizz_Buzz(number)
    #     self.assertEqual(is_fizzbuzz,"Buzz")
    
    def test_give_9_is_fizz(self):
        number = 9
        is_fizzbuzz = get_Fizz_Buzz(number)
        self.assertEqual(is_fizzbuzz,"Fizz")

    def test_give_65_is_fizzbuzz(self):
        number = 60
        is_fizzbuzz = get_Fizz_Buzz(number)
        self.assertEqual(is_fizzbuzz,"FizzBuzz")
        


