from survey import AnonymousSurvey

question = "what language did you first learn to speak?"
my_surevy = AnonymousSurvey(question)

my_surevy.show_question()
print("enter 'q' at any time to quit.\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_surevy.store_response(response)
print("\nthank you to everyone who participated in the survey!")
my_surevy.show_results()