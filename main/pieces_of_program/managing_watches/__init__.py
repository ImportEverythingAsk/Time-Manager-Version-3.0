from tkinter import *
from ..database import watches
from . import add_watch
from .watch_menu.__init__ import Watch_Menu
from .watch_menu import watch_button
from .watch_menu import watch_settings
# import sys
# sys.path.append("..")
# from ..database import alarms
# from main.database import watches

class Managing_Watches():
    watch_total = 0
    def __init__(self, app):
        self.app = app
    def render(self):
        self.managing_watches_frame = LabelFrame(self.app.root, bg=self.app.secondary_bg_color, padx=3, pady=5)
        self.managing_watches_frame.grid(row=0, column=0)
        # watch_menu = Watch_Menu(managing_watches_frame, self.database)

        add_watch_button = Button(self.managing_watches_frame, text="Add Watch", padx=60, bg=self.app.add_watch_bg_color,
                                  fg=self.app.add_watch_fg_color)
        add_watch_button.grid(row=0, column=0)
        add_watch_button.bind('<Button-1>', lambda e:self.popup_making())
        self.menu = Watch_Menu(self.app)
        self.menu.render()

    def popup_making(self):
        window = add_watch.render(self.app.root)
        done = Button(window, text="Add Watch", command=lambda: self.make_watch_managing_watch_side(window))
        done.grid(row=4, column=1)


    def make_watch_managing_watch_side(self, window):
        self.watch_total += 1

        watch_name = add_watch.give_info()[0]
        total_alarms = add_watch.give_info()[1]

        # Database 3.0

        prepared_data = [watch_name, "Edit Notes Here", total_alarms, 0, self.watch_total, 1]
        watches.insert_watch(prepared_data)

        if int(total_alarms) >= 19:
            # Too many alarms to fit on the screen Add popup
            return

            # Might need code below sometime
            # watch_total += 1
            #
            # try:
            #     c.execute("SELECT watch_id FROM watches WHERE was_last_opened = 1")
            #     selected = c.fetchone()[0] - 1
            #     watch_list[selected].close()
            # except:
            #     pass
            # watch = Watch(c, conn, root, frame_of_watches, watch_name, total_alarms, watch_total, add_window,
            #               this_is_a)

            #         NEED TO: Make watch buttons on GUI Leftside
        self.menu.make_new_menu_watches(watch_name, self.watch_total)
        self.app.make_watch_app_side(watch_name, total_alarms, self.watch_total)
        window.destroy()
