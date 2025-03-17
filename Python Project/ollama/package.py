import ollama
import json

# Initialize the Ollama Client
client = ollama.Client()

# Define the model and the input prompt
model = "deepseek-r1" # Replace with you model name
prompt = "what to eat tonight?"

response = client.generate(model = model, prompt= prompt)

# Print the response from the model
print("Response from ollama:")
print(response.response)