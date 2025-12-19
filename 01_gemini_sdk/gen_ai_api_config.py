import dotenv

from google import genai

# Load environment variables from .env file
dotenv.load_dotenv()

# Schema definition
schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "story": {"type": "string"}
    },
    "required": ["title", "story"]
}

safety_settings = [
    genai.types.SafetySetting(
        category=genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=genai.types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    ),
    genai.types.SafetySetting(
        category=genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=genai.types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    ),
]

# Prepare config
config = genai.types.GenerateContentConfig(
    system_instruction="You are a Georgian writer. Be poetic.",
    # temperature=1.0,
    # max_output_tokens=2024,
    # response_mime_type="application/json",
    # response_schema=schema,
    # safety_settings=safety_settings
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="დამიწერე პატარა მოთხრობა ქუთაისზე",
    config=config
)

print(response.text)
