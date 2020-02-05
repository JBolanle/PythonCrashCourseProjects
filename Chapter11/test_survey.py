import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for AnonymousSurvey class"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods
        """
        question = "What language did you first learnt to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Yoruba', 'French']

    def test_store_single_response(self):
        """Tests that a single response gets stored properly"""
        question = "What language did you first learnt to speak?"
        self.my_survey.store_respones(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_multiple_responses(self):
        """Tests that more than one response gets stored properly"""
        for response in self.responses:
            self.my_survey.store_respones(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()