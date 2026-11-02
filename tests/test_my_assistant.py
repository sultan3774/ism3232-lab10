from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup


def make_assistant():
    schedule = {"monday": "9:00 am and 2:30 pm", "friday": ""}
    return AppointmentAssistant("Robin", AppointmentLookup(schedule))


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
    assert "Robin" in assistant.history[1]["content"]
