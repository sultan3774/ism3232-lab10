# my_assistant.py
# Author: Sultan Ali


class AppointmentAssistant:  # Define the appointment assistant.
    def __init__(self, name, tool, model, instructions):  # Accept its settings.
        self.name = name  # Store the assistant's name.
        self.tool = tool  # Store the appointment lookup tool.
        self.model = model  # Store the model for other questions.
        self.instructions = instructions  # Store facts and model instructions.
        self.history = []  # Create a separate conversation history.

    def respond(self, message):  # Handle one message.
        self.history.append({"role": "user", "content": message})  # Save the request.
        reply = self.choose_reply(message)  # Choose the response.
        self.history.append({"role": "assistant", "content": reply})  # Save the reply.
        return reply  # Return the response.

    def choose_reply(self, message):  # Apply rules before asking the model.
        text = message.lower()  # Match keywords regardless of capitalization.
        if "book" in text or "cancel" in text:  # Staff handle schedule changes.
            return "I can't change the schedule. I'm passing you to the front desk."
        if "time" in text or "available" in text:  # Use the tool for open times.
            day = self.tool.find_day(text)  # Find the requested day.
            if day is None:  # Ask for a day if none was found.
                return "Which day? I can check Monday, Wednesday, or Friday."
            times = self.tool.times_for(day)  # Get times from the tool.
            if not times:  # Handle days without open times.
                return f"No open times found for {day}. Please contact the front desk."
            return f"Open times on {day}: {times}."  # Return the tool's result.
        return self.model_reply()  # Send other questions to the model.

    def model_reply(self):  # Handle the model's answer.
        reply = self.model.reply(self.instructions, self.history)  # Send context.
        if reply is None:  # Provide a safe response if the model cannot answer.
            return (
                "Sorry, I can't answer that right now. Please contact the front desk."
            )
        return reply  # Return the model's answer.
