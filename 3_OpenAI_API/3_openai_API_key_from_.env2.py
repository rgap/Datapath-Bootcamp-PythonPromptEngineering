from dotenv import load_dotenv
from openai import OpenAI

# # Load the .env file
load_dotenv()

client = OpenAI()

input_text = "Once upon a time"

# Make API call
result = client.completions.create(
    model="gpt-3.5-turbo-instruct",  # This is one of the GPT-3 models
    prompt=f"Complete this sentence: {input_text}",
)

# Print the response
print("result.choices:\n", result.choices)

print("result.choices[0].text:\n", result.choices[0].text)

print("response:\n", input_text + result.choices[0].text)
