import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("GEMINI_API_KEY not found in .env")
    exit()


client = genai.Client(
    api_key=api_key
)


response = client.interactions.create(
    model="gemini-3.5-flash",
    input="Suggest 3 vegetarian South Indian dishes under 200 rupees."
)


print("\nGemini Response:\n")
print(response.output_text)