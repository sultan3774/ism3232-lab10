# my_tool.py
# Author: Sultan Ali


class AppointmentLookup:
    # Create a tool that stores the available appointment times.
    def __init__(self, schedule):
        self.schedule = schedule  # Keep the schedule for later lookups.

    # Find a known day in the user's message.
    def find_day(self, text):
        for day in self.schedule:  # Check each day in the schedule.
            if day in text.lower():  # Match without depending on capital letters.
                return day  # Return the matching day.
        return None  # No known day was mentioned.

    # Look up the available times for a day.
    def times_for(self, day):
        if day in self.schedule:  # Check that the day exists.
            return self.schedule[day]  # Return its available times.
        return None  # The day is not in the schedule.
