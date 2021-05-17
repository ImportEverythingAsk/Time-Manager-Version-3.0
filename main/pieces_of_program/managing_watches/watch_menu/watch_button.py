from tkinter import *
class Watch_Button:
    def __init__(self, app, frame_of_watches, watch_name, watch_id):
        self.app = app
        self.frame_of_watches = frame_of_watches
        self.watch_name = watch_name
        self.watch_id = watch_id
    def render(self):
        self.watch_name_button = Button(self.frame_of_watches, text=self.watch_name, width=34, anchor=W,
                                        bg=self.app.selected_watch_bg_color, command=self.watch_clicked)
        self.watch_name_button.grid(row=self.watch_id, column=0, pady=1)

    def watch_clicked(self):
        # Changing color of previously highlighted watch
        # AND Change which watch is opened in watch menu
        self.app.watch_manager.menu.current_watch_id = self.watch_id
        self.app.watch_manager.menu.change_current_watch(self)

        # Highlight this watch
        self.highlight()
        self.app.watch_manager.menu.current_watch_settings.highlight()


    def highlight(self):
        self.watch_name_button.config(bg=self.app.selected_watch_bg_color)
    def unhighlight(self):
        self.watch_name_button.config(bg=self.app.watches_list_color)