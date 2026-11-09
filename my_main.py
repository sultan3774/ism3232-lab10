# my_main.py
# Author: Sultan Ali

from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Robin, a friendly appointment assistant.
Answer in one short sentence.
The office is at 40 Harbor Street, on the second floor.
Customers should bring a photo ID and last year's tax return.
Only state facts that appear in these instructions.
If you do not know, say you do not know and refer the customer to the front desk."""

SCHEDULE = {
    "monday": "9:00 am and 2:30 pm",
    "wednesday": "10:00 am and 1:00 pm",
    "friday": "11:00 am and 3:00 pm",
}

tool = AppointmentLookup(SCHEDULE)
model = OllamaModel(MODEL_NAME)
assistant = AppointmentAssistant("Robin", tool, model, INSTRUCTIONS)

print("Type a message, or type quit to stop.")
message = input("You: ")

while message != "quit":
    print(f"{assistant.name}: {assistant.respond(message)}")
    message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
