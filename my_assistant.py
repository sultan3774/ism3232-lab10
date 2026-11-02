# my_assistant.py
# Author: Sultan Ali


class AppointmentAssistant:  # Define the appointment assistant.
    def __init__(self, name, tool):  # Set up each assistant.
        self.name = name  # Store its name for greetings.
        self.tool = tool  # Store the tool used to find appointment times.
        self.history = []  # Give this assistant its own conversation history.

    def respond(self, message):  # Handle one message and record both sides.
        self.history.append({"role": "user", "content": message})  # Save the request.
        reply = self.choose_reply(message)  # Choose a response.
        self.history.append({"role": "assistant", "content": reply})  # Save the reply.
        return reply  # Send the response back to the caller.

    def choose_reply(self, message):  # Select a response using keyword rules.
        text = message.lower()  # Make keyword matching ignore capital letters.
        if "book" in text or "cancel" in text:  # Staff must change appointments.
            return "I can't change the schedule. I'm passing you to the front desk."
        if "time" in text or "available" in text:  # Use the tool for time requests.
            day = self.tool.find_day(text)  # Look for a known day.
            if day is None:  # Ask for details when no known day is found.
                return "Which day? I can check Monday, Wednesday, or Friday."
            times = self.tool.times_for(day)  # Look up that day's times.
            if not times:  # Handle a missing or empty result.
                return f"No open times found for {day}. Please contact the front desk."
            return f"Open times on {day}: {times}."  # Show the available times.
        if "hello" in text:  # Respond to a greeting.
            return f"Hello! I'm {self.name}. Ask me which times are available."
        return "I'm not sure how to help with that. I can list open times."
