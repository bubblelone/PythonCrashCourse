import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "what language did you first learn to speak?"
        self.my_surevy = AnonymousSurvey(question)
        self.responses = ['english', 'spanish', 'mandarin']


    def test_store_single_response(self):

        self.my_surevy.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_surevy.responses)

    def test_store_three_responses(self):

        for response in self.responses:
            self.my_surevy.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_surevy.responses)


if __name__ == '__main__':
    unittest.main()