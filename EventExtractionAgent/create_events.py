from EventExtractionAgent.event_extraction_agent import event_extraction


question = "Please provide the name of you next event, the date, and who is going. "

while True:
    user_prompt = input(question)

    if not user_prompt:
        continue

    print(event_extraction(user_prompt))

    quit_app = input("Would you like to schedule anything else? (y/n) ")

    if quit_app and quit_app.lower() == 'n':
        break
