# Lab 10: Appointment Assistant

My assistant helps users check available appointment times for a small office.
It uses a separate tool to look up times and saves each user message and reply in its history.
This is a mock assistant that uses keyword rules and a sample schedule, not a real AI model or booking system.
Booking and cancellation requests go to the front desk because a staff member must confirm schedule changes.
If it used real customer data, saving private information in the conversation history could expose that information to other people.

## Lab 11: Appointment Assistant with a Model

The model correctly answered "Where is the office?" with 40 Harbor Street, on the second floor. It also told the customer to bring a photo ID and last year's tax return. When I asked about business taxes, it said it did not know and referred me to the front desk. I kept appointment times in the lookup tool so they come from the schedule. Booking and cancellation requests stay in code because a staff member must handle schedule changes.