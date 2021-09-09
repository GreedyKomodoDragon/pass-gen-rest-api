from functions.pass_strength import pass_strength
import unittest
from functions.pass_gen import pass_gen

class TestPasswordGeneration(unittest.TestCase):

    def setUp(self) -> None:
        self.symbols = "!\"#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~"
        self.lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.higher_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"

        self.gen_function = pass_gen
        self.strength_function = pass_strength

    def test_length(self):
        """
        Should create a password with the required length sent
        """

        # Less than 8, should throw an exception
        with self.assertRaises(ValueError) as context:
            self.gen_function(7, False)

        self.assertTrue('Not enough letters for an effective password' in str(context.exception))

        # With 8 letters given with no symbols, but should have lower, upper and number
        password = self.gen_function(8, False)
        self.assertTrue(len(password) == 8)
        

    def test_contains_no_symbols(self):
        """
        Test for checking that each attribute is returned but not symbols
        """

        password_without_sym = self.gen_function(8, False)
        self.assertTrue(not any([sym in password_without_sym for sym in self.symbols]))
        self.assertTrue(any([low in password_without_sym for low in self.lower_alphabet]))
        self.assertTrue(any([upper in password_without_sym for upper in self.higher_alphabet]))

    def test_contains_symbols(self):
        """
        Test for checking that each attribute is returned
        """

        password_with_sym = self.gen_function(8, True)
        self.assertTrue(any([sym in password_with_sym for sym in self.symbols]))
        self.assertTrue(any([low in password_with_sym for low in self.lower_alphabet]))
        self.assertTrue(any([upper in password_with_sym for upper in self.higher_alphabet]))








        

if __name__ == "__main__":
    unittest.main()