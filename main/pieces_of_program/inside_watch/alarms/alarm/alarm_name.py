from tkinter import *
class Alarm_Name:
    def __init__(self, alarm_box, default_name):
        self.alarm_box = alarm_box
        self.default_name = default_name
    def render(self):
        self.namevar = StringVar(self.alarm_box)
        self.namevar.set("Alarms name")
        name_entry = Entry(self.alarm_box, textvariable=self.namevar)
        name_entry.grid(row=0, column=0)