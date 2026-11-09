from mock_model import MockModel
from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup


class SilentModel:
    """A model that returns no answer."""

    def reply(self, instructions, history):
        return None


def make_assistant(model=None):
    if model is None:
        model = MockModel()
    schedule = {"monday": "9:00 am and 2:30 pm", "friday": ""}
    return AppointmentAssistant(
        "Robin",
        AppointmentLookup(schedule),
        model,
        "Be friendly. If you do not know, refer the customer to the front desk.",
    )


def test_available_times():
    assistant = make_assistant()
    assert (
        assistant.respond("What times are available on Monday?")
        == "Open times on monday: 9:00 am and 2:30 pm."
    )


def test_missing_day():
    assistant = make_assistant()
    assert "Which day?" in assistant.respond("What is available?")


def test_empty_times():
    assistant = make_assistant()
    assert "No open times" in assistant.respond("What times are available on Friday?")


def test_booking_goes_to_staff():
    assistant = make_assistant()
    assert "front desk" in assistant.respond("Please book Monday at 9")


def test_unknown_request():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("Do you validate parking?")


def test_history_records_both_messages():
    assistant = make_assistant()
    assistant.respond("hello")
    assert len(assistant.history) == 2
    assert assistant.history[0] == {"role": "user", "content": "hello"}
    assert assistant.history[1]["role"] == "assistant"
    assert assistant.history[1]["content"] == "Hello! How can I help you today?"


def test_safe_reply_when_model_has_no_answer():
    assistant = make_assistant(SilentModel())
    assert (
        assistant.respond("hello")
        == "Sorry, I can't answer that right now. Please contact the front desk."
    )


def test_times_work_without_model_answer():
    assistant = make_assistant(SilentModel())
    assert (
        assistant.respond("What times are available on Monday?")
        == "Open times on monday: 9:00 am and 2:30 pm."
    )


def test_booking_handoff_without_model_answer():
    assistant = make_assistant(SilentModel())
    assert "front desk" in assistant.respond("Please book Monday at 9")
