import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for AnonymousSurvey class"""

    def test_store_single_response(self):
        """Tests that a single response gets stored properly"""
        question = "What language did you first learnt to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_respones('English')

        self.assertIn('English', my_survey.responses)

unittest.main()