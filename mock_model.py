# mock_model.py
# Author: Sultan Alsereidi


class MockModel:
    """A stand-in for an AI model with fixed replies."""

    def reply(self, instructions, history):
        """Return a fixed reply based on the last message."""
        last_message = history[-1]["content"].lower()
        if "hello" in last_message:
            return "Hello! How can I help you today?"
        return "I'm not sure how to help with that. I can check an order or stock."
