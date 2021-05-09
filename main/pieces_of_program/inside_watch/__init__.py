from tkinter import *
from . import file_watch_name
from . import notes
from .alarms.__init__ import All_Alarms
class Inside_Watch():
    def __init__(self, root, database):
        self.root = root
        self.database = database
    def make_watch_inside_watch_side(self, watch_name, total_alarms, watch_id):
        watch_frame = LabelFrame(self.root)
        watch_frame.grid(row=0, column=1)

        file_watch_name.render(watch_frame, watch_name)
        all_alarms = All_Alarms(watch_frame, total_alarms, watch_id)
        all_alarms.render_alarms()
        notes.render(watch_frame)