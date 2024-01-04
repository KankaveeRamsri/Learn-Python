from coe_number.Staircase import display_staircase
import unittest

class StaircaseTest(unittest.TestCase):
    def test_give_2_h_should_be_hh(self):
        n = 2
        pattern = "#"
        expected_output = " #\n" + "##"
        
        result = display_staircase(n, pattern)
        
        self.assertEqual(result, expected_output, f"Should be {expected_output}")