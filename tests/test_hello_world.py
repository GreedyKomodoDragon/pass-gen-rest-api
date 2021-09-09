import unittest

class TestHelloWorld(unittest.TestCase):

    def setUp(self) -> None:
        self.message = "hello world"

    def test_message(self):
        self.assertEqual(self.message, "hello world")

if __name__ == "__main__":
    unittest.main()