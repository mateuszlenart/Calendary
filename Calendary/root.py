import tkinter as tk
from datetime import datetime, time
from EventClass import Event

root = tk.Tk()
root.title("Calendary")

view_of_calendary = tk.Frame(root)
view_of_calendary.pack()

label = tk.Label(root, text="Hej")
label.pack()

button = tk.Button(root, text="Push Me")
button.pack()

entry = tk.Entry(root)
entry.pack()

events = [
    Event("Spotkanie z klientem", datetime(2023, 6, 29), time(14, 59), "Omówienie projektu"),
    Event("Urodziny", datetime(2023, 7, 10), time(18, 30), "Zorganizować przyjęcie"),
    Event("Wyjazd na wakacje", datetime(2023, 8, 5), time(9, 0), "Spakować walizki"),
]

def check_events():
    now = datetime.now()
    for event in events:
        event_datetime = event.get_datetime()
        if event_datetime > now:
            time_diff = event_datetime - now
            minutes_left = int(time_diff.total_seconds() / 60)
            if minutes_left < 10:
                return event
    return None

def push_the_button():
    event = check_events()
    if event is not None:
        event.show_notification("Przypomnienie", f"Nadchodzi wydarzenie: {event.title}")

button.config(command=push_the_button)

root.mainloop()