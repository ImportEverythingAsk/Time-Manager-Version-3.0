from tkinter import *
class Watch_Button:
    def __init__(self, frame_of_watches, watch_name, watch_id):
        self.frame_of_watches = frame_of_watches
        self.watch_name = watch_name
        self.watch_id = watch_id
    def make_watch_button(self):
        self.watch_name_button = Button(self.frame_of_watches, text=self.watch_name, width=23, anchor=W, bg="gold",
                                        command=self.watch_clicked)
        self.watch_name_button.grid(row=self.watch_id, column=0)
    def watch_clicked(self):
        print("need to make watch clicked function")
