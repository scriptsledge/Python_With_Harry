from openai import OpenAI

# Install OpenAI library: pip install openai

# Initialize OpenAI client with your API key
client = OpenAI(api_key="Your API")

# Generate a chat completion
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Specify the model
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "what is coding"}
    ]
)

# Output the assistant's response
print(completion.choices[0].message.content)
