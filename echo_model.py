# echo_model.py
# Author: Sultan Ali


class EchoModel:
    """A model that repeats the last message."""

    def reply(self, instructions, history):
        return "You said: " + history[-1]["content"]
