from tools.convert_currency import convert_currency

from google.adk.agents import Agent

root_agent = Agent(
    name="currency_agent",
    model="gemini-2.0-flash",
    description="An agent that converts currencies using a tool.",
    instruction=(
        "You are a helpful assistant.\n"
        "If the user asks about currency conversion, "
        "call the convert_currency tool.\n"
        "If the tool returns an error, explain it politely.\n"
        "Keep answers short and clear."
    ),
    tools=[convert_currency],
)
