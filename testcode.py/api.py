import openai_secret_manager
import openai

# Authenticate with OpenAI API
# openai_secret_manager.get_secret("manish")
openai.api_key = "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"

# Define function to search using Chat GPT
def search(query):
    prom = f"What is {query}?"
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prom,
      max_tokens=400,
      n=1,
      stop=None,
      temperature=0.7,
    )
    return response.choices[0].text.strip()

# Take user input
query = input("What do you want to search for? ")

# Search using Chat GPT and print response
response = search(query)
print(response)


