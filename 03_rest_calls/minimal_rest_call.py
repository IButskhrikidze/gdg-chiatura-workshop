import os
import requests
import dotenv

dotenv.load_dotenv()

API_KEY = os.environ["GOOGLE_API_KEY"]
MODEL = "gemini-2.5-flash"

url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
params = {"key": API_KEY}

payload = {
    "contents": [
        {
            "role": "user",
            "parts": [{"text": "Convert 50 USD to GEL"}]
        }
    ],
    "tools": [
        {
            "functionDeclarations": [
                {
                    "name": "convert_currency",
                    "description": "Convert currency",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "amount": {"type": "number"},
                            "from_currency": {"type": "string"},
                            "to_currency": {"type": "string"}
                        },
                        "required": ["amount", "from_currency", "to_currency"]
                    }
                }
            ]
        }
    ]
}

response = requests.post(url, params=params, json=payload, timeout=20)
response.raise_for_status()

data = response.json()
print(data)
# print(data["candidates"][0]["content"]["parts"][0]["text"])
