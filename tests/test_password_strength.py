import unittest
from functions.pass_strength import pass_strength

class TestPasswordStrength(unittest.TestCase):

    def setUp(self) -> None:
        self.symbols = "!\"#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~"
        self.lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.higher_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"

        self.strength_function = pass_strength

    def test_values(self):
        """
        Should Assign points to the following passwords
        """
        # blank
        self.assertEqual(self.strength_function(""), 0)
        self.assertEqual(self.strength_function("       "), 0)

        # contains at least one number
        for number in self.numbers:
            self.assertEqual(self.strength_function(number), 5)

        # Contains at least one lowercase
        for lower in self.lower_alphabet:
            self.assertEqual(self.strength_function(lower), 5)

        # Contains at least one uppercase
        for higher in self.higher_alphabet:
            self.assertEqual(self.strength_function(higher), 5)

        # Contains at least one symbol 
        for symbol in self.symbols:
            self.assertEqual(self.strength_function(symbol), 10)

        # Contains at least 5 unique characters and lowercase
        self.assertEqual(self.strength_function("abcde"), 15)

        # Is at least 8 characters long and lowercase
        self.assertEqual(self.strength_function("abcdefgh"), 20)

        # Is at least 8 characters long, lower and higher
        self.assertEqual(self.strength_function("Abcdefgh"), 25)

        # Is at least 8 characters long, lower, higher and number 
        self.assertEqual(self.strength_function("Abcdefgh1"), 30)

        # Is at least 13 characters with lowercase
        self.assertEqual(self.strength_function("aaaaaaaaaaaaa"), 20)

        # Is at least 13 characters with lower, higher, symbol and 5 unique
        self.assertEqual(self.strength_function("Abcdefghi12345;'"), 50)


        

if __name__ == "__main__":
    unittest.main()