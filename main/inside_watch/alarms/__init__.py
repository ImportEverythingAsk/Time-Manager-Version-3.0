from tkinter import *
from .alarm.__init__ import Alarm
import math
class All_Alarms:
    def __init__(self, watch_frame, total_alarms):
        self.watch_frame = watch_frame
        self.total_alarms = total_alarms
        print("making alarms")
    def render_alarms(self):
        alarm_frames = LabelFrame(self.watch_frame)
        alarm_frames.grid(row=1, column=0)

        alarms_by_three = int(self.total_alarms) / 3
        floored = math.floor(alarms_by_three)
        remaining_number_of_alarms = int(round((alarms_by_three - floored) * 3))
        for fullrow in range(0, floored):
            for column in range(0, 3):
                currentAlarm = Alarm(alarm_frames, fullrow, column)
                currentAlarm.make_alarm()
                print("going")
                # if self.this_is_a == "make":
                #     currentAlarm.make_data()
                # else:
                #     currentAlarm.load_data(column + 1)
                # alarmData = currentAlarm.make_data()

        for alarm in range(0, remaining_number_of_alarms):
            currentAlarm = Alarm(alarm_frames, floored, alarm)
            currentAlarm.make_alarm()
            # if self.this_is_a == "make":
            #     currentAlarm.make_data()
            # else:
            #     currentAlarm.load_data(alarm + 1)

