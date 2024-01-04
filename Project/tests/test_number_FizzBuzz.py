from coe_number.number_FizzBuzz import is_Fizz_Buzz
import unittest


class FizzBuzzListTest(unittest.TestCase):
    def test_give_1_2_3_is_fizzbuzz(self):
        fizzbuzz_list = [3,6]
        is_fizzbuzz = is_Fizz_Buzz(fizzbuzz_list)
        self.assertTrue(is_fizzbuzz)
