from tkinter import *
from ...database import watches
from ...database import alarms
class Watch_Settings:
    def __init__(self, app, frame_of_watches, watch_name, watch_id):
        self.app = app
        self.frame_of_watches = frame_of_watches
        self.watch_name = watch_name
        self.watch_id = watch_id

    def render(self):

        self.watch_settings_button = Button(self.frame_of_watches, text=":", command=self.open_watch_settings,
                                            bg=self.app.selected_watch_bg_color)
        self.watch_settings_button.grid(row=self.watch_id, column=1, pady=1)


    def open_watch_settings(self):
        self.popup_window = Toplevel()
        self.popup_window.iconbitmap("../Images/Stopwatch Time Manager.ico")
        self.popup_window.title("Watch Settings")

        change_watch_name_label = Label(self.popup_window, text="Change Watch Name?")
        change_watch_name_label.grid(row=0, column=0)

        self.watch_name_var = StringVar()
        change_watch_name_entry = Entry(self.popup_window, textvariable=self.watch_name_var, width=50)
        change_watch_name_entry.grid(row=0, column=1)
        change_watch_name_entry.insert(0, self.watch_name)

        def checkbox_action():
            if self.run_next_alarm_immediately_var.get() == 0:
                yes_or_no_label = Label(self.popup_window, text="No")
                yes_or_no_label.grid(row=1, column=2)
            else:
                yes_or_no_label = Label(self.popup_window, text="Yes")
                yes_or_no_label.grid(row=1, column=2)

        run_next_alarm_label = Label(self.popup_window,
                                     text="Do you want to run your next alarm immediately \n after the"
                                          " previous one ends?")
        run_next_alarm_label.grid(row=1, column=0)
        self.run_next_alarm_immediately_var = IntVar()
        yes_or_no_label = Label(self.popup_window, text="No")
        yes_or_no_label.grid(row=1, column=2)
        run_next_alarm_immediately_box = Checkbutton(self.popup_window, variable=self.run_next_alarm_immediately_var,
                                                     command=checkbox_action)
        run_next_alarm_immediately_box.grid(row=1, column=1)

        save_settings_button = Button(self.popup_window, text="Save Settings", command=self.save_settings)
        save_settings_button.grid(row=11, column=0)

        remove_watch_button = Button(self.popup_window, text="Remove Watch", command=self.remove_watch_action)
        remove_watch_button.grid(row=10, column=0)

    def save_settings(self):
        self.watch_name = self.watch_name_var.get()
        self.run_next_alarm_immediately = self.run_next_alarm_immediately_var.get()

        self.app.inside_watch.file_watch_name.change_watch_name(self.watch_name)
        self.app.watch_manager.menu.change_a_name_of_a_watch(self.watch_name, self.watch_id)


        prepared_data = [self.watch_name,  self.run_next_alarm_immediately, self.watch_id]
        watches.update_data(prepared_data)

        self.popup_window.destroy()
    def remove_watch_action(self):
        # Removing data from the database
        watches.delete_watch(self.watch_id)
        alarms.delete_alarms(self.watch_id)

        # Clearing a watch from the screen (GUI right side)
        if self.watch_id == self.app.inside_watch.current_all_alarms.watch_id:
            self.app.inside_watch.clear()

        # Removing the menu buttons from the screen
        self.app.watch_manager.menu.watch_button_dict[self.watch_id].watch_name_button.grid_remove()
        self.watch_settings_button.grid_remove()
        new_key = self.app.watch_manager.menu.current_watch_id
        # Highlighting the menu buttons of the watch that is automatically opened.
        if self.app.watch_manager.menu.current_watch_id == self.watch_id:
            new_key = self.check_highlight()
        self.app.watch_manager.menu.remove_and_change_watches(self.watch_id, new_key)
        self.popup_window.destroy()

    def check_highlight(self):
        list_verison = list(self.app.watch_manager.menu.watch_button_dict)
        if len(self.app.watch_manager.menu.watch_button_dict) == 1:
            print("Was only 1 watch")
            key = 0
        elif len(list_verison[0:list_verison.index(self.watch_id)]) > 0:
            print("Going to watch above")
            key = list_verison[list_verison.index(self.watch_id) - 1]
        else:
            print("Going to watch below")

            key = list_verison[list_verison.index(self.watch_id) + 1]


        if key > 0:
            self.app.watch_manager.menu.watch_button_dict[key].highlight()
            self.app.watch_manager.menu.watch_settings_button_dict[key].highlight()
        self.app.watch_manager.menu.current_watch_id = key
        return key

    def highlight(self):
        self.watch_settings_button.config(bg=self.app.selected_watch_bg_color)
    def unhighlight(self):
        self.watch_settings_button.config(bg=self.app.watches_list_color)