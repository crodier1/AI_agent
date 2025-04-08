from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

completion = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {"role": "system", "content": "You're a helpful assistant"},
        {"role": "user",
         "content": "Write a limerick about python programming language."
         }
    ]
)

response = completion.choices[0].message.content

print(response)




