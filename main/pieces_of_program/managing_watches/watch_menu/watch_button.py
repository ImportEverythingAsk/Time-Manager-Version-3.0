from tkinter import *
class Watch_Button:
    def __init__(self, app, frame_of_watches, watch_name, watch_id):
        self.app = app
        self.frame_of_watches = frame_of_watches
        self.watch_name = watch_name
        self.watch_id = watch_id
    def render(self):
        self.watch_name_button = Button(self.frame_of_watches, text=self.watch_name, width=23, anchor=W,
                                        bg=self.app.selected_watch_bg_color, command=self.watch_clicked)
        self.watch_name_button.grid(row=self.watch_id, column=0, pady=1)

    def set_watch_lists(self, watch_button_list, watch_settings_button_list):
        self.watch_button_list= watch_button_list
        self.watch_settings_button_list = watch_settings_button_list

    def watch_clicked(self):
        print("need to make watch clicked function")
