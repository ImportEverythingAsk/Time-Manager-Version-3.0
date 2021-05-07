from tkinter import *
class Watch_Settings:
    def __init__(self, frame_of_watches, watch_name, watch_id):
        self.frame_of_watches = frame_of_watches
        self.watch_name = watch_name
        self.watch_id = watch_id

    def make_watch_settings(self):

        self.watch_settings_button = Button(self.frame_of_watches, text=":", command=self.open_watch_settings,
                                            bg="gold")
        self.watch_settings_button.grid(row=self.watch_id, column=1)

    def open_watch_settings(self):
        print("need to make open watch settings")