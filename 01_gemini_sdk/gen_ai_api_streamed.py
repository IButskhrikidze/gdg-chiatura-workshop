import dotenv

from google import genai

# Load environment variables from .env file
dotenv.load_dotenv()

client = genai.Client()

stream = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="დამიწერე პატარა მოთხრობა ქუთაისზე"
)

for chunk in stream:
    print(chunk.text, end="")
