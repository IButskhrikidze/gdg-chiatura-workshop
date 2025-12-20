import dotenv

from google import genai

dotenv.load_dotenv()

client = genai.Client()

prompt = (
    "Create a picture of city Kutaisi in the winter season"
)

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("assets/generated_image.png")
