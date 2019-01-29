import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "what language did you first learn to speak?"
        my_surevy = AnonymousSurvey(question)



    def test_store_single_response(self):
        question = "what language did you first learn to speak?"
        my_surevy = AnonymousSurvey(question)
        my_surevy.store_response('english')
        self.assertIn('english', my_surevy.responses)

    def test_store_three_responses(self):
        question = "what language did you first learn to speak?"
        my_surevy = AnonymousSurvey(question)
        responses = ['english','spanish','mandarin']
        for response in responses:
            my_surevy.store_response(response)
        for response in responses:
            self.assertIn(response, my_surevy.responses)


if __name__ == '__main__':
    unittest.main()