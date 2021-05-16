from tkinter import *
from .watch_button import Watch_Button
from .watch_settings import Watch_Settings
from ...database import watches
class Watch_Menu:
    current_watch_id = 0
    watch_button_dict = {}
    watch_settings_button_dict = {}
    def __init__(self, app):
        self.app = app
    def render(self):
        menu_labelframe = LabelFrame(self.app.watch_manager.managing_watches_frame, bg=self.app.secondary_bg_color)
        menu_labelframe.grid(row=1, column=0)
        menu_label = Label(menu_labelframe, text="Watches Menu", padx=52, anchor=W, bg=self.app.watch_menu_label_bg_color)
        menu_label.grid(row=1, column=0)

        self.frame_of_watches = LabelFrame(self.app.watch_manager.managing_watches_frame, padx=5, pady=5,
                                           bg=self.app.watches_list_color)
        self.frame_of_watches.grid(row=2, column=0)
    def make_new_menu_watches(self, watch_name, watch_id):
        # Changing which watch the database says is currently on
        if self.current_watch_id != 0:
            watches.update_was_last_opened_column(self.current_watch_id)

            # Changing the color of the previously selected watch back to normal
            self.watch_button_dict[self.current_watch_id].watch_name_button.config(bg=self.app.watches_list_color)
            self.watch_settings_button_dict[self.current_watch_id].watch_settings_button.config(bg=self.app.watches_list_color)

        self.current_watch_button = Watch_Button(self.app, self.frame_of_watches, watch_name, watch_id)
        self.current_watch_button.render()
        self.current_watch_settings = Watch_Settings(self.app, self.frame_of_watches, watch_name, watch_id)
        self.current_watch_settings.render()

        self.watch_button_dict[watch_id] = self.current_watch_button
        self.watch_settings_button_dict[watch_id] = self.current_watch_settings

        self.current_watch_id = watch_id
    def change_a_name_of_a_watch(self, new_name, row_number):
        self.watch_button_dict[row_number - 1].watch_name_button.config(text=new_name)

    def remove_and_change_watches(self, index, new_watch_key):
        del self.watch_button_dict[index]
        del self.watch_settings_button_dict[index]

        try:
            self.current_watch_button = self.watch_button_dict[new_watch_key]
            self.current_watch_settings = self.watch_settings_button_dict[new_watch_key]
        except:
            pass

    def change_current_watch(self, now_opened_watch):
        self.current_watch_button.unhighlight()
        self.current_watch_settings.unhighlight()

        self.current_watch_button = now_opened_watch
        self.current_watch_settings = self.watch_settings_button_dict[self.current_watch_id]


