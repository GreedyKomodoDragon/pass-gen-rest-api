import app
import unittest
import json


class TestAPIRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

        self.symbols = "!\"#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~"

    def test_status_code_pass_gen(self):
        """
        Testing API routes can be called for pass gen
        """
        response_invalid = self.app.get('/api/v1/passgen/7/0')
        self.assertEqual(response_invalid.status_code, 204)

        response = self.app.get('/api/v1/passgen/8/0')
        self.assertEqual(response.status_code, 200)

    def test_content_pass_gen(self):
        """
        Testing that the body return is a valid password
        """

        # With no symbol
        response_without_sym = self.app.get('/api/v1/passgen/8/0')
        json_response = json.loads(response_without_sym.data.decode('UTF-8'))
        password_without_sym = json_response["password"]

        self.assertTrue(not any([sym in password_without_sym for sym in self.symbols]))
        self.assertTrue(len(password_without_sym) == 8)

        # With symbol
        response_with_sym = self.app.get('/api/v1/passgen/8/1')
        json_response = json.loads(response_with_sym.data.decode('UTF-8'))
        password_with_sym = json_response["password"]

        self.assertTrue(any([sym in password_with_sym for sym in self.symbols]))
        self.assertTrue(len(password_without_sym) == 8)

    
    def test_status_code_pass_strength(self):
        """
        Testing API routes can be called for pass strength
        """
        response = self.app.post('/api/v1/strength', data={
            "password": ""
        })
        
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/api/v1/strength')
        self.assertEqual(response.status_code, 204)

    def test_content_pass_gen(self):
        """
        Testing that the body return is a valid password
        """

        # Blank
        response_without_sym = self.app.post('/api/v1/strength', data={
            "password": ""
        })

        json_response = json.loads(response_without_sym.data.decode('UTF-8'))
        score = json_response["score"]

        self.assertEqual(score, 0)

        # With letters - Abcdefgh1 = 30 points
        response_with_sym = self.app.post('/api/v1/strength', data={
            "password": "Abcdefgh1"
        })
        json_response = json.loads(response_with_sym.data.decode('UTF-8'))
        score = json_response["score"]

        self.assertEqual(score, 30)


    

if __name__ == '__main__':
    unittest.main()