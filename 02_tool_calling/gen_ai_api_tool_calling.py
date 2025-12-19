import dotenv

from tools.convert_currency import convert_currency

from google import genai

# Load environment variables from .env file
dotenv.load_dotenv()

# Prepare Tool
convert_currency_decl = genai.types.FunctionDeclaration(
    name="convert_currency",
    description="Convert money between currencies using recent exchange rates.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "amount": {
                "type": "number",
                "description": "Amount of money to convert"
            },
            "from_currency": {
                "type": "string",
                "description": "Base currency code, e.g. USD"
            },
            "to_currency": {
                "type": "string",
                "description": "Target currency code, e.g. GEL"
            },
        },
        "required": ["amount", "from_currency", "to_currency"],
    },
)

tools = [genai.types.Tool(function_declarations=[convert_currency_decl])]

# Prepare config
config = genai.types.GenerateContentConfig(
    system_instruction="You are a helpful assistant. "
                       "If the user asks for currency conversion, call the convert_currency tool. "
                       "If the tool fails, explain the error and ask for a different currency code.",
    tools=[convert_currency],
    # automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(disable=True),
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How much GEL is 50 USD?",
    config=config
)

print(response.text)
