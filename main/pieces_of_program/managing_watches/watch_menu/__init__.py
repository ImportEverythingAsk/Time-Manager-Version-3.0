from tkinter import *
from .watch_button import Watch_Button
from .watch_settings import Watch_Settings
class Watch_Menu:
    watch_button_list = []
    watch_settings_button_list = []
    def __init__(self, app, managing_watches_frame):
        self.app = app
        self.managing_watches_frame = managing_watches_frame
    def render(self):
        menu_labelframe = LabelFrame(self.managing_watches_frame)
        menu_labelframe.grid(row=1, column=0)
        menu_label = Label(menu_labelframe, text="Watches Menu", width=26, anchor=W)
        menu_label.grid(row=1, column=0)

        self.frame_of_watches = LabelFrame(self.managing_watches_frame)
        self.frame_of_watches.grid(row=2, column=0)
    def make_new_menu_watches(self, watch_name, watch_id):

        current_watch_button = Watch_Button(self.frame_of_watches, watch_name, watch_id)
        current_watch_button.render()
        current_watch_settings = Watch_Settings(self.app, self.frame_of_watches, watch_name, watch_id)
        current_watch_settings.render()

        self.watch_button_list.append(current_watch_button)
        self.watch_settings_button_list.append(current_watch_settings)

        current_watch_button.set_watch_lists(self.watch_button_list, self.watch_settings_button_list)
        current_watch_settings.set_watch_lists(self.watch_button_list, self.watch_settings_button_list)
    def change_a_name_of_a_watch(self, new_name, row_number):
        self.watch_button_list[row_number - 1].watch_name_button.config(text=new_name)




