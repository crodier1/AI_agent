import json
import google.generativeai as genai
from Dependencies.get_api_key import get_gemini_key
from fuzzywuzzy import fuzz

genai.configure(api_key=get_gemini_key())
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')


def manage_calendar_events(calendar_events, new_event):
    """
    Manages a list of calendar events, adding, updating, or leaving them unchanged
    based on the presence and similarity of a new event.

    Args:
        calendar_events: A list of dictionaries, where each dictionary represents a calendar event.
        new_event: A dictionary representing the event to be added or updated.

    Returns:
        A tuple containing:
            - The updated list of calendar events.
            - A string describing the action taken ("added", "updated", or "no change").
    """

    if not calendar_events:
        return [new_event], "added"  # If the list is empty, just add the event

    for i, existing_event in enumerate(calendar_events):

        similarity_ratio = fuzz.ratio(new_event["name"].lower(), existing_event["name"].lower())
        if similarity_ratio > 80:
            calendar_events[i] = new_event
            return calendar_events, "updated"

        # if events_are_similar(existing_event, new_event):
        #     updated_event = merge_event_details(existing_event, new_event)
        #     calendar_events[i] = updated_event
        #     return calendar_events, "updated"

    calendar_events.append(new_event)
    return calendar_events, "added"


def events_are_similar(event1, event2):
    """
    Determines if two events are considered "similar" enough to warrant an update.
    This is a crucial part where you can use the language model to help.

    Args:
        event1: The first event dictionary.
        event2: The second event dictionary.

    Returns:
        True if the events are similar, False otherwise.
    """

    prompt = f"""
        Are these two calendar events referring to the same event?
        Consider that slight variations in wording, capitalization, and date changes within a few days should be considered the same event.
        Examples:
        - "Meeting at 2 PM" vs. "Meeting at 2:00 PM" (same)
        - "John's birthday" vs. "Birthday of John" (same)
        - "Project deadline" vs. "Project deadline moved to next week" (same)
        - "Job Fair" vs. "job fair" (same)
        - "Job Fair on 4/20" vs. "Job Fair on 4/21" (same)
        - "Job Fair on 4/20" vs. "Job Fair on 5/10" (different)

        Return "True" if they are the same event, or "False" if they are different events.

        Event 1: {json.dumps(event1)}
        Event 2: {json.dumps(event2)}

        Answer:
        """

    response = model.generate_content(prompt)
    answer = response.text.strip().lower()
    return "true" in answer  # Simple check, refine as needed


def merge_event_details(existing_event, new_event):
    """
    Merges details from the new event into the existing event.
    This is another area where the language model could assist with intelligent merging.

    Args:
        existing_event: The existing event dictionary.
        new_event: The new event dictionary.

    Returns:
        The merged event dictionary.
    """

    merged_event = existing_event.copy()  # Start with a copy to avoid modifying the original

    if new_event.get("date"):
        merged_event["date"] = new_event["date"]  # Update date if provided

    merged_participants = list(set(existing_event.get("participants", []) + new_event.get("participants", [])))
    merged_event["participants"] = merged_participants

    return merged_event


def normalize_event_name(name):
    return name.lower().strip()
