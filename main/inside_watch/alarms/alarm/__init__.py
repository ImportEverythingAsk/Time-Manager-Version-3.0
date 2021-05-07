from tkinter import *
from ...alarms import images_handler
from .alarm_clock import Alarm_Clock
from .alarm_name import Alarm_Name
from .button import ButtonObject
from . import settings_popup
class Alarm:
    def __init__(self, alarms_frame, row, column):
        self.alarms_frame = alarms_frame
        self.row = row
        self.column = column

    def make_alarm(self):
        print("making alrmns")

        from_images_handler = images_handler.give_images()
        images = from_images_handler[0]
        disabled_images = from_images_handler[1]
        setting_image = from_images_handler[2]

        alarm_box = Frame(self.alarms_frame)
        alarm_box.grid(row=self.row, column=self.column)

        alarm_name = Alarm_Name(alarm_box, "Example Name")
        alarm_name.make_alarm_name()


        self.alarm_clock = Alarm_Clock(alarm_box, "0:02:05")
        self.alarm_clock.make_alarm_clock()

        self.buttonbox = LabelFrame(alarm_box)
        self.buttonbox.grid(row=2, column=0)
        self.reset_button = ButtonObject(self.buttonbox, images['reset'], disabled_images['reset'], DISABLED,
                                         command=self.reset)
        self.reset_button.button.grid(row=0, column=0)
        self.play_button = ButtonObject(self.buttonbox, images['play'], disabled_images['play'], NORMAL,
                                        command=self.play)
        self.play_button.button.grid(row=0, column=1)
        self.pause_button = ButtonObject(self.buttonbox, images['pause'], disabled_images['pause'], DISABLED,
                                         command=self.pause)
        self.pause_button.button.grid(row=0, column=2)
        settings = Button(self.buttonbox, image=setting_image, command=lambda: settings_popup.open_settings_popup())
        settings.grid(row=0, column=3)

        return alarm_box
    def make_commands(self):
        print("need to make commands")


    def play(self):
        self.alarm_clock.start()
        if self.reset_button.button['state'] == DISABLED:
            self.reset_button.toggle()
        self.play_button.toggle()
        self.pause_button.toggle()
        self.buttonbox.after(1000, self.countdown)

    def pause(self):
        self.alarm_clock.stop()
        if self.reset_button.button['state'] == DISABLED:
            self.reset_button.toggle()
        self.play_button.toggle()
        self.pause_button.toggle()

        # self.stop = True

    def reset(self):
        self.alarm_clock.reset()
        if self.play_button.button['state'] == DISABLED:
            self.play_button.toggle()
            self.pause_button.toggle()
        self.reset_button.toggle()

        # self.stop = True

        #Changing Time
        # self.remaining_time = self.beginning_time
        # self.digital.config(text=self.beginning_time)

    def countdown(self):
        if self.alarm_clock.stop:
            return
        remaining_time = self.alarm_clock.getRemainingTime()
        self.alarm_clock.digital.config(text=remaining_time)
        self.buttonbox.after(1000, self.countdown)