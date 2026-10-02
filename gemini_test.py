import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Gemini API key not found")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send a test request to Gemini
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Say hello in one short sentence."
)

# Display Gemini response
print("Gemini Response:")
print(interaction.output_text)