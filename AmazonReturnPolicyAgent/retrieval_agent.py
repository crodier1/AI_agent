from Dependencies.AmazonReturnPolicy import get_retail_return_policy
import json
import google.generativeai as genai  # Changed the import

from Dependencies.get_api_key import get_gemini_key


def create_return_policy_agent(return_policy_dict):
    """
    Creates an agent that answers questions about a retail return policy.

    Args:
        return_policy_dict (dict): A dictionary containing the retail return policy.

    Returns:
        function: An agent function that takes a user prompt (question)
                  and returns an answer based on the return policy.
    """

    def agent(prompt):
        """
        Answers a user's question about the return policy.

        Args:
            prompt (str): The user's question about the return policy.

        Returns:
            str: An answer to the user's question, based on the provided
                 return policy dictionary.
        """

        # Convert the dictionary to a string format that Gemini can understand
        context = f"Here is the retail return policy: {json.dumps(return_policy_dict)}"

        # Initialize the Gemini model
        genai.configure(api_key=get_gemini_key())
        model = genai.GenerativeModel('gemini-1.5-pro')  # Use genai

        # Craft a detailed prompt for Gemini, including context and instructions
        gemini_prompt = f"""
        You are a helpful customer service agent. 
        Answer the user's question about the return policy.
        Here is the return policy:
        {context}

        User Question: {prompt}
        """

        # Get the response from the Gemini model
        response = model.generate_content(gemini_prompt)
        return response.text

    return agent


return_policy_agent = create_return_policy_agent(get_retail_return_policy())

question = "Hi, how can I help you with Amazon's return policy? "

while True:
    user_prompt = input(question)

    if not user_prompt:
        continue

    print(return_policy_agent(user_prompt))

    quit_chat = input("Is there anything else I can help you with? (y/n) ")

    if quit_chat and quit_chat.lower() == 'n':
        print("Have a great day!")
        break

    question = "Is there anything else I can help you with? "





