import openai
import chatbot.config as config

# Set your API key for the custom model


# Initialize the OpenAI API client with your custom model ID
openai.api_key = config.API_KEY

# Create a prompt and make an API request
prompt = "what medical tax back can I get"
response = openai.Completion.create(
    model="g-8Ol05SYLL-irish-tax-assistant",  # Replace with your custom model ID #
    prompt=prompt,
    max_tokens=50  # Adjust this based on your requirements
)

# Get the generated response
generated_text = response.choices[0].text

print(generated_text)
