# my_main.py
# Author: Sultan Ali

from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup

SCHEDULE = {
    "monday": "9:00 am and 2:30 pm",
    "wednesday": "10:00 am and 1:00 pm",
    "friday": "11:00 am and 3:00 pm",
}

tool = AppointmentLookup(SCHEDULE)
assistant = AppointmentAssistant("Robin", tool)

print("Type a message, or type quit to stop.")
message = input("You: ")

while message != "quit":
    print(f"{assistant.name}: {assistant.respond(message)}")
    message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
