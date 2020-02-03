from survey import AnonymousSurvey

question = "What language did you first learn to speak?"

lang_survey = AnonymousSurvey(question)
lang_survey.show_question()

print("Enter 'q' at any time to quit. \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    lang_survey.store_respones(response)

print("\nThank's for participating in the survey!\n")
lang_survey.show_results()