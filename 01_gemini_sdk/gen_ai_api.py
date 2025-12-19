import dotenv

from google import genai

# Load environment variables from .env file
dotenv.load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="დამიწერე პატარა მოთხრობა ქუთაისზე",
)

print(response.text)
