from tkinter import *
from pygame import mixer
from ...alarms import images_handler
from .alarm_clock import Alarm_Clock
from .alarm_name import Alarm_Name
from .button import ButtonObject
from . import settings_popup
from ....database import alarms
class Alarm:
    alarm_name = "Alarms Name"
    # beginning_time = "0:02:05"
    # remaining_time = "0:02:05"
    is_specific_time_checked = 0
    notify_dropdown_time = "None"
    specific_notify_time = "None"
    alarm_sound = "Classic Alarm"
    default_time = "00:00:05"
    def __init__(self, app, alarms_frame, row, column, watch_id):
        self.app = app
        self.alarms_frame = alarms_frame
        self.row = row
        self.column = column
        self.watch_id = watch_id

    def render(self):
        from_images_handler = images_handler.give_images()
        images = from_images_handler[0]
        disabled_images = from_images_handler[1]
        setting_image = from_images_handler[2]


        extra_design_frame = LabelFrame(self.alarms_frame, background=self.app.alarm_border_color, relief=FLAT, borderwidth=5)
        extra_design_frame.grid(row=self.row, column=self.column, padx=1, pady=1)
        alarm_box = Frame(extra_design_frame, borderwidth=15, background=self.app.alarm_bg_color)
        alarm_box.grid(row=self.row, column=self.column)

        self.alarm_name = Alarm_Name(self.app, alarm_box, "Example Name")
        self.alarm_name.render()


        self.alarm_clock = Alarm_Clock(self.app, alarm_box, self.default_time)
        self.alarm_clock.render()

        self.buttonbox = Frame(alarm_box)
        self.buttonbox.grid(row=2, column=0, padx=2, pady=5)
        self.reset_button = ButtonObject(self.app, self.buttonbox, images['reset'], disabled_images['reset'], DISABLED,
                                         command=self.reset)
        self.reset_button.button.grid(row=0, column=0)
        self.play_button = ButtonObject(self.app, self.buttonbox, images['play'], disabled_images['play'], NORMAL,
                                        command=self.play)
        self.play_button.button.grid(row=0, column=1)
        self.pause_button = ButtonObject(self.app, self.buttonbox, images['pause'], disabled_images['pause'], DISABLED,
                                         command=self.pause)
        self.pause_button.button.grid(row=0, column=2)
        settings = Button(self.buttonbox, image=setting_image,
                          bg=self.app.timer_buttons_color, command=lambda: settings_popup.render(self, self.app))
        settings.grid(row=0, column=3)

        self.alarm_id = alarms.insert_alarm(self.get_prepared_data())
        return alarm_box

    def get_prepared_data(self):
        prepared_data = [self.row, self.column, self.alarm_name.namevar.get(), self.alarm_clock.initial_time,
                         self.alarm_clock.remaining_time, self.is_specific_time_checked, self.notify_dropdown_time,
                         self.specific_notify_time, self.alarm_sound, self.watch_id]
        return prepared_data

    def play(self):
        self.alarm_clock.start()
        if self.reset_button.button['state'] == DISABLED:
            self.reset_button.toggle()
        self.play_button.toggle()
        self.pause_button.toggle()
        self.buttonbox.after(1000, self.countdown)

    def pause(self):
        self.alarm_clock.stop_countdown()
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


        #Changing Time
        # self.remaining_time = self.beginning_time
        # self.digital.config(text=self.beginning_time)

    def countdown(self):
        if self.alarm_clock.stop:
            return
        remaining_time = self.alarm_clock.getRemainingTime()
        self.alarm_clock.digital.config(text=remaining_time)
        if remaining_time == "00:00:00":
            mixer.init()
            mixer.music.load("../Sounds/FIZZZZZ.wav")
            mixer.music.play()
        self.buttonbox.after(1000, self.countdown)