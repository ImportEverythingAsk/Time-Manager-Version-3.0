from tkinter import *
from datetime import *

class Alarm_Clock:
    stop = True
    def __init__(self, alarm_box, default_time):
        self.alarm_box = alarm_box
        self.default_time = default_time
        self.initial_time = default_time
        self.final_time = default_time
        self.remaining_time = default_time

    def render(self):
        self.digitalbox = LabelFrame(self.alarm_box)
        self.digitalbox.grid(row=1, column=0)

        self.digital = Label(self.digitalbox, text=self.initial_time)
        self.digital.grid(row=0, column=0)

    def start(self):
        self.stop = False
        start_time = datetime.today()
        time_parts = self.initial_time.split(':')
        interval = timedelta(hours=int(time_parts[0]), minutes=int(time_parts[1]), seconds=int(time_parts[2])+1)

        self.final_time = start_time + interval

    def stop_countdown(self):
        self.stop = True

    def reset(self):
        self.stop = True
        self.digital.config(text=self.initial_time)
    def getRemainingTime(self):
        current_time = datetime.today()
        print(self.final_time - current_time)
        remaining = (self.final_time - current_time).seconds

        if (remaining <= 0):
            self.stop = True
            return "00:00:00"

        tempTime = datetime.strptime("01/01/1970", "%m/%d/%Y")

        remainingTime = tempTime + timedelta(seconds=remaining)
        print(remainingTime.strftime("%H:%M:%S"))
        self.remaining_time = remainingTime.strftime("%H:%M:%S")
        return self.remaining_time
