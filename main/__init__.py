from tkinter import *
from pieces_of_program.managing_watches import Managing_Watches
from pieces_of_program.inside_watch import Inside_Watch
from pieces_of_program.inside_watch.alarms import images_handler
from pieces_of_program.database.__init__ import Database


class MainApplication:
    watch_total = 0

    def __init__(self):
        self.render()

    def render(self):
        # Tkinter side setup
        self.root = Tk()
        self.root.config(bg="grey25")
        self.root.geometry("1920x1080")
        self.root.title("Time Manager Version 3")
        self.root.iconbitmap("../Images/Stopwatch Time Manager.ico")

        # Setting up the database
        self.database = Database()
        self.database.data_setup()

        # Images setup
        images_handler.handle_images()

        # Setting up and rendering parts of the program
        self.watch_manager = Managing_Watches(self.root, self.database, self)
        self.watch_manager.render()

        self.inside_watch = Inside_Watch(self.root, self.database)

        self.root.protocol("WM_DELETE_WINDOW", self.app_closed)
        self.root.mainloop()

    def make_watch_main_app_side(self, watch_name, total_alarms, watch_id):
        self.watch_total += 1
        self.inside_watch.make_watch_inside_watch_side(watch_name, total_alarms, watch_id)

    def app_closed(self):
        self.database.closing_program()
        self.root.destroy()


main_app = MainApplication()
