from tkinter import *
from .alarm.__init__ import Alarm
import math
class All_Alarms:
    def __init__(self, app, watch_frame, total_alarms, watch_id):
        self.app = app
        self.watch_frame = watch_frame
        self.total_alarms = total_alarms
        self.watch_id = watch_id
    def render_alarms(self):
        alarm_frames = Frame(self.watch_frame, bg=self.app.secondary_bg_color)
        alarm_frames.grid(row=1, column=0, pady=20, padx=20)

        alarms_by_three = int(self.total_alarms) / 3
        floored = math.floor(alarms_by_three)
        remaining_number_of_alarms = int(round((alarms_by_three - floored) * 3))
        for fullrow in range(0, floored):
            for column in range(0, 3):
                currentAlarm = Alarm(self.app, alarm_frames, fullrow, column, self.watch_id)
                currentAlarm.render()
                # if self.this_is_a == "make":
                #     currentAlarm.make_data()
                # else:
                #     currentAlarm.load_data(column + 1)
                # alarmData = currentAlarm.make_data()

        for alarm in range(0, remaining_number_of_alarms):
            currentAlarm = Alarm(self.app, alarm_frames, floored, alarm, self.watch_id)
            currentAlarm.render()
            # if self.this_is_a == "make":
            #     currentAlarm.make_data()
            # else:
            #     currentAlarm.load_data(alarm + 1)

