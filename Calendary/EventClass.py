from datetime import datetime
from plyer import notification

class Event():
    def __init__(self, title, date, time, description):
        self.title=title
        self.date=date
        self.time=time
        self.description=description
    def edit_title(self,new_title):
        self.title=new_title
    def edit_date(self, new_date):
        self.date=new_date
    def edit_time(self,new_time):
        self.time = new_time
    def edit_descr(self,new_descr):
        self.description=new_descr
    def get_datetime(self):
        return datetime.combine(self.date, self.time)

    def show_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            timeout=10,
        )

    def __str__(self):
        return f"Event: {self.title}\nDate: {self.get_datetime()}\nDescription: {self.description}"



