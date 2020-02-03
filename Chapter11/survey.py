class AnonymousSurvey():
    """Collects answers to an anonymous survey"""

    def __init__(self, question):
        """Stores the question in creates a list to store responses"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the question survey"""
        print(question)

    def store_respones(self, new_response):
        """Store a single response in the list"""
        self.response.append(new_response)

    def show_results(self):
        """Prints the results in the list"""
        print("Survey results: ")
        for response in responses:
            print("- " + response)