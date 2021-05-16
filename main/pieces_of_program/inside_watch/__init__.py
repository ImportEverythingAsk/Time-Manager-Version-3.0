from tkinter import *
from .file_watch_name import File_Watch_Name
from . import notes
from .alarms.__init__ import All_Alarms
class Inside_Watch():
    def __init__(self, app):
        self.app = app
    def make_watch_inside_watch_side(self, watch_name, total_alarms, watch_id):
        self.watch_frame = Frame(self.app.root, bg="grey15", background="grey15")
        self.watch_frame.grid(row=0, column=1)


        self.file_watch_name = File_Watch_Name(self.app, self.watch_frame, watch_name)
        self.file_watch_name.render()
        self.current_all_alarms = All_Alarms(self.app, self.watch_frame, total_alarms, watch_id)
        self.current_all_alarms.render_alarms()
        notes.render(self.app, self.watch_frame)

    def clear(self):
        self.watch_frame.grid_remove()