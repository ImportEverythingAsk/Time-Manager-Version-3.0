from tkinter import *
from ...database import watches
class Watch_Settings:
    def __init__(self, app, frame_of_watches, watch_name, watch_id):
        self.app = app
        self.frame_of_watches = frame_of_watches
        self.watch_name = watch_name
        self.watch_id = watch_id

    def render(self):

        self.watch_settings_button = Button(self.frame_of_watches, text=":", command=self.open_watch_settings,
                                            bg="gold")
        self.watch_settings_button.grid(row=self.watch_id, column=1)

    def set_watch_lists(self, watch_button_list, watch_settings_button_list):
        self.watch_button_list= watch_button_list
        self.watch_settings_button_list = watch_settings_button_list

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
        self.popup_window.destroy()