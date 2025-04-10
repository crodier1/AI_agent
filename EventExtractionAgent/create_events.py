import json

from EventExtractionAgent.event_extraction_agent import event_extraction, event_is_valid, confirm_event

question = "Please provide the name of you next event, the date, and who is going. "

while True:
    user_prompt = input(question)

    if not user_prompt:
        continue

    response = json.loads(event_extraction(user_prompt))

    if not event_is_valid(response):
        print(response['error'])
        continue

    validate_event = input(confirm_event(response))

    if validate_event and validate_event.lower() == 'n':
        continue

    quit_app = input("Would you like to schedule anything else? (y/n) ")

    if quit_app and quit_app.lower() == 'n':
        break
