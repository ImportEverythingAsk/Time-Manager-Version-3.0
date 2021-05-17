from tkinter import *
from tkinter import messagebox
from ..database import watches
from . import add_watch
from .watch_menu.__init__ import Watch_Menu
from .watch_menu import watch_button
from .watch_menu import watch_settings

class Managing_Watches():
    watch_total = 0
    def __init__(self, app):
        self.app = app
    def render(self):
        self.managing_watches_frame = LabelFrame(self.app.root, bg=self.app.secondary_bg_color, padx=3, pady=5)
        self.managing_watches_frame.grid(row=0, column=0)

        add_watch_button = Button(self.managing_watches_frame, text="Add Watch", padx=60, bg=self.app.add_watch_bg_color,
                                  fg=self.app.add_watch_fg_color)
        add_watch_button.grid(row=0, column=0)
        add_watch_button.bind('<Button-1>', lambda e:self.popup_making())
        self.menu = Watch_Menu(self.app)
        self.menu.render()

    def popup_making(self):
        window = add_watch.render(self.app)
        done = Button(window, text="Add Watch", command=lambda: self.make_watch_managing_watch_side(window),
                      bg=self.app.selected_watch_bg_color)
        done.grid(row=4, column=1)


    def make_watch_managing_watch_side(self, window):
        self.watch_total += 1

        watch_name = add_watch.give_info()[0]
        total_alarms = add_watch.give_info()[1]

        # Database 3.0

        prepared_data = [watch_name, "Edit Notes Here", total_alarms, 0, self.watch_total, 1]
        watches.insert_watch(prepared_data)

        test_failed = self.check_entered_text_test(total_alarms, len(watch_name))
        if test_failed == True:
            return

        self.menu.make_new_menu_watches(watch_name, self.watch_total)
        self.app.make_watch_app_side(watch_name, total_alarms, self.watch_total)
        window.destroy()

    def check_entered_text_test(self, total_alarms, name_length):
        # Here we are checking the what the user entered into the total alarms to see if what the user entered was a number 1-18.
        failed = False

        # Too many characters in the the name of the watch to fit on the menu.
        if name_length > 42:
            messagebox.showerror(title="Time Manager", message="The text you entered for your watch name"
                                                               " was too long (More than 42 characters. "
                                                               "Reached beyond the end of the entry you entered "
                                                               "you watch name in.) "
                                                               "Please, try again.")
            return True

        # Checking the user actually entered a integer
        try:
            integer_verison = int(total_alarms)
        except:
            # Add popup to tell the user he entered some text that wasn't a whole number.
            messagebox.showerror(title="Time Manager", message="The text you entered for your total number of alarms"
                                                               " for this watch included characters that were not "
                                                               "whole numbers. Please, try again.")
            failed = True
            return failed

        # Checking the user entered a number for 0 alarms
        if integer_verison == 0:
            messagebox.showerror(title="Time Manager", message="The number you entered for your total number of alarms"
                                                               " for this watch was 0. Please, try again.")
            failed = True

        # Checking if the user entered a number for less than 0 alarms.
        elif integer_verison < 0:
            messagebox.showerror(title="Time Manager", message="The number you entered for your total number of alarms"
                                                               " for this watch was a negative number."
                                                               " Please, try again.")
            failed = True

        # Too many alarms to fit on the screen
        elif integer_verison >= 19:
            messagebox.showerror(title="Time Manager", message="The number you entered for your total number of alarms"
                                                               " for this watch was a number greater than 18. "
                                                               " No more than 18 alarms will fit on the screen."
                                                               " Please, try again.")
            failed = True

        return failed
