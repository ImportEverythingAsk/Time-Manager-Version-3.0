from tkinter import *
def render(watch_frame, watch_name):
    inside_label_frame_for_label = LabelFrame(watch_frame)
    inside_label_frame_for_label.grid(row=0, column=0)
    # Allow option to change watch's name.
    inside = Label(inside_label_frame_for_label, text=watch_name)
    inside.grid(row=0, column=0)