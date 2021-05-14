from tkinter import *
class File_Watch_Name:
    def __init__(self, app, watch_frame, watch_name):
        self.app = app
        self.watch_frame = watch_frame
        self.watch_name = watch_name
    def render(self):
        inside_label_frame_for_label = LabelFrame(self.watch_frame)
        inside_label_frame_for_label.grid(row=0, column=0)
        # Allow option to change watch's name.
        self.inside = Label(inside_label_frame_for_label, text=self.watch_name, bg=self.app.alarm_labels_color)
        self.inside.grid(row=0, column=0)
    def change_watch_name(self, new_name):
        self.inside.config(text=new_name)