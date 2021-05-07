from tkinter import *
from . import add_watch
from .watch_menu.__init__ import Watch_Menu
from .watch_menu import watch_button
from .watch_menu import watch_settings
# import sys
# sys.path.append("..")
# from ..database import alarms
# from main.database import watches

class Managing_Watches():
    def __init__(self, root, database, main_app):
        self.root = root
        self.database = database
        self.main_app = main_app
    def render(self):
        self.managing_watches_frame = LabelFrame(self.root)
        self.managing_watches_frame.grid(row=0, column=0)
        # watch_menu = Watch_Menu(managing_watches_frame, self.database)

        add_watch_button = Button(self.managing_watches_frame, text="Add Watch", padx=60)
        add_watch_button.grid(row=0, column=0)
        add_watch_button.bind('<Button-1>', lambda e:self.popup_making())
        menu = Watch_Menu(self.managing_watches_frame)
        menu.make_menu()

    def popup_making(self):
        window = add_watch.open_adding_watch_popup(self.root)
        done = Button(window, text="Add Watch", command=lambda: self.make_watch_managing_watch_side(window))
        done.grid(row=4, column=1)


    def make_watch_managing_watch_side(self, window):
        watch_name = add_watch.give_info()[0]
        total_alarms = add_watch.give_info()[1]

        # Might need code below sometime
        # watch_total += 1

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
        self.watch_menu = Watch_Menu(self.managing_watches_frame)
        self.watch_menu.make_menu()
        self.watch_menu.make_new_menu_watches(watch_name, total_alarms)
        self.main_app.make_watch_main_app_side(watch_name, total_alarms)
        window.destroy()

        # alarms.make_alarms(total_alarms)
            # watch_list.append(watch)
            # for watch in watch_list:
            #     watch.set_new_watch_list(watch_list)


            # Do ALL updating/inserting database work for watches here i guess
            # c.execute("UPDATE watches set was_last_opened = 0 WHERE was_last_opened = 1")
            # conn.commit()
            # watch.make_data()







    #
    # was_last_opened = 1
    # notes = "Edit notes here."
    # run_next_alarm_immediately = 0
    #
    # def __init__(self, c, conn, root, frame_of_watches, watch_name, total_alarms, watch_id, add_window, this_is_a):
    #     self.c = c
    #     self.conn = conn
    #     self.root = root
    #     self.frame_of_watches = frame_of_watches
    #     self.watch_name = watch_name
    #     self.total_alarms = total_alarms
    #     self.watch_id = watch_id
    #     self.add_window = add_window
    #     self.this_is_a = this_is_a
    #     real_watch_id = self.watch_id
    #     self.render()
    #
    # def set_new_watch_list(self, watch_list, is_delete):
    #     self.watch_list = watch_list
    #     try:
    #         self.c.execute("SELECT watch_id FROM watches WHERE was_last_opened = 1")
    #         selected = self.c.fetchone()[0]
    #         print("first select: " + str(selected))
    #         selectedsub1 = selected - 1
    #         print("Subtract 1: " + str(selectedsub1))
    #         self.watch_list[selectedsub1].watch_name_button.config(bg="SystemButtonFace")
    #         self.watch_list[selectedsub1].watch_settings_button.config(bg="SystemButtonFace")
    #     except:
    #         pass
    #
    # def watch_clicked(self):
    #     # Making watch on GUI left side
    #     self.watch_name_button = Button(self.frame_of_watches, text=self.watch_name, width=23, anchor=W, bg="gold",
    #                                     command=self.watch_clicked)
    #     self.watch_settings_button = Button(self.frame_of_watches, text=":", command=self.open_watch_settings,
    #                                         bg="gold")
    #     self.watch_name_button.grid(row=self.watch_id, column=0)
    #     self.watch_settings_button.grid(row=self.watch_id, column=1)
    #     try:
    #         self.set_new_watch_list(self.watch_list)
    #     except:
    #         pass
    #     self.c.execute("SELECT watch_id FROM watches WHERE was_last_opened = 1")
    #     selected = self.c.fetchone()[0] - 1
    #     # print(selected)
    #     self.watch_list[selected].close()
    #     self.c.execute("UPDATE watches SET was_last_opened = 0")
    #     self.c.execute("UPDATE watches SET was_last_opened = 1 WHERE watch_id = " + str(self.watch_id))
    #     self.conn.commit()
    #     self.load_data()
    #     self.this_is_a = "load"
    #     self.render()
    #
    # def render(self):
    #     print("rendering")
    #
    #     self.watch_name_button = Button(self.frame_of_watches, text=self.watch_name, width=23, anchor=W, bg="gold",
    #                                     command=self.watch_clicked)
    #     self.watch_settings_button = Button(self.frame_of_watches, text=":", command=self.open_watch_settings,
    #                                         bg="gold")
    #     self.watch_name_button.grid(row=self.watch_id, column=0)
    #     self.watch_settings_button.grid(row=self.watch_id, column=1)
    #     # Making inside watch at the top of the screen
    #     # INSIDE WATCH IS WAT WE LOOKING FOR
    #     self.inside_watch = LabelFrame(self.root)
    #     self.inside_watch.grid(row=0, column=1)
    #     # inside_watch.grid_remove()
    #     # inside_watch = LabelFrame(self.root)
    #     # inside_watch.grid(row=0, column=1)
    #     self.inside_label_frame_for_label = LabelFrame(self.inside_watch)
    #     self.inside_label_frame_for_label.grid(row=0, column=0)
    #     # Allow option to change watch's name.
    #     self.inside = Label(self.inside_label_frame_for_label, text=self.watch_name)
    #     self.inside.grid(row=0, column=0)
    #
    #     # Making alarm part GUI right side
    #     alarm_frame = LabelFrame(self.inside_watch)
    #     alarm_frame.grid(row=1, column=0)
    #
    #     alarms_by_three = self.total_alarms / 3
    #     floored = math.floor(alarms_by_three)
    #     remaining_number_of_alarms = int(round((alarms_by_three - floored) * 3))
    #     for fullrow in range(0, floored):
    #         for column in range(0, 3):
    #             currentAlarm = Alarm(self.c, self.conn, self.root, alarm_frame, fullrow, column, self.watch_id)
    #             if self.this_is_a == "make":
    #                 currentAlarm.make_data()
    #             else:
    #                 currentAlarm.load_data(column + 1)
    #             currentAlarm.render()
    #             # alarmData = currentAlarm.make_data()
    #
    #     for alarm in range(0, remaining_number_of_alarms):
    #         currentAlarm = Alarm(self.c, self.conn, self.root, alarm_frame, floored, alarm, self.watch_id)
    #         if self.this_is_a == "make":
    #             currentAlarm.make_data()
    #         else:
    #             currentAlarm.load_data(alarm + 1)
    #         currentAlarm.render()
    #     # Might need this below in the future
    #     self.add_window.destroy()
    #
    #     # Making notes
    #
    #     notev = StringVar(self.root)
    #     notev.set("Edit notes here.")
    #     notes = LabelFrame(self.inside_watch)
    #     notes.grid(row=2, column=0)
    #     notetop = Label(notes, text="Notes", width=50, anchor=W)
    #     notetop.grid(row=0, column=0)
    #     noteentry = Entry(notes, width=44, textvariable=notev)
    #     noteentry.grid(row=1, column=0)
    #     buttonsave = Button(notes, text="Save notes", command=lambda: self.save_notes(notev.get()))
    #     buttonsave.grid(row=2, column=0)
    #
    # def save_notes(self, the_notes):
    #     self.notes = the_notes
    #     self.update_data()
    #
    # def save_settings(self):
    #     self.watch_name = self.watch_name_var.get()
    #     self.run_next_alarm_immediately = self.run_next_alarm_immediately_var.get()
    #
    #     self.inside.grid_forget()
    #     self.inside = Label(self.inside_label_frame_for_label, text=self.watch_name)
    #     self.inside.grid(row=0, column=0)
    #
    #     self.update_data()
    #     self.popup_window.destroy()
    #
    # def open_watch_settings(self):
    #     self.popup_window = Toplevel()
    #     self.popup_window.iconbitmap("Images/Stopwatch Time Manager.ico")
    #     self.popup_window.title("Watch Settings")
    #
    #     change_watch_name_label = Label(self.popup_window, text="Change Watch Name?")
    #     change_watch_name_label.grid(row=0, column=0)
    #
    #     self.watch_name_var = StringVar()
    #     change_watch_name_entry = Entry(self.popup_window, textvariable=self.watch_name_var, width=50)
    #     change_watch_name_entry.grid(row=0, column=1)
    #     change_watch_name_entry.insert(0, self.watch_name)
    #
    #     def checkbox_action():
    #         if self.run_next_alarm_immediately_var.get() == 0:
    #             yes_or_no_label = Label(self.popup_window, text="No")
    #             yes_or_no_label.grid(row=1, column=2)
    #         else:
    #             yes_or_no_label = Label(self.popup_window, text="Yes")
    #             yes_or_no_label.grid(row=1, column=2)
    #
    #     run_next_alarm_label = Label(self.popup_window,
    #                                  text="Do you want to run your next alarm immediately \n after the"
    #                                       " previous one ends?")
    #     run_next_alarm_label.grid(row=1, column=0)
    #     self.run_next_alarm_immediately_var = IntVar()
    #     yes_or_no_label = Label(self.popup_window, text="No")
    #     yes_or_no_label.grid(row=1, column=2)
    #     run_next_alarm_immediately_box = Checkbutton(self.popup_window, variable=self.run_next_alarm_immediately_var,
    #                                                  command=checkbox_action)
    #     run_next_alarm_immediately_box.grid(row=1, column=1)
    #
    #     save_settings_button = Button(self.popup_window, text="Save Settings", command=self.save_settings)
    #     save_settings_button.grid(row=11, column=0)
    #
    #     remove_watch_button = Button(self.popup_window, text="Remove Watch", command=self.remove_watch_action)
    #     remove_watch_button.grid(row=10, column=0)
    #
    # def remove_watch_action(self):
    #     print("removing")
    #     self.inside_watch.grid_remove()
    #     self.watch_name_button.grid_remove()
    #     self.watch_settings_button.grid_remove()
    #     if len(self.watch_list) == 1:
    #         print("Only 1 watch")
    #         print(len(self.watch_list))
    #         print(self.watch_id)
    #     elif len(self.watch_list) == self.watch_id:
    #         print("Going to watch above")
    #         print(len(self.watch_list))
    #         print(self.watch_id)
    #         self.watch_list[self.watch_id - 1].load_data()
    #         self.watch_list[self.watch_id - 1].render()
    #     else:
    #         print("Going to watch below")
    #         print(len(self.watch_list))
    #         print(self.watch_id)
    #         self.watch_list[self.watch_id].load_data()
    #         self.watch_list[self.watch_id].render()
    #
    #     self.c.execute("DELETE FROM watches WHERE watch_id = " + str(self.watch_id))
    #     self.c.execute("DELETE FROM alarms where watch_id =" + str(self.watch_id))
    #     self.conn.commit()
    #
    #     # Updating the list of watches for other watches list of the watches.
    #     del self.watch_list[self.watch_id - 1]
    #     for watch in self.watch_list:
    #         watch.set_new_watch_list(self.watch_list, "delete")
    #
    #     self.popup_window.destroy()
    #
    # def load_data(self):
    #     sql_load = "SELECT rowid, * FROM watches WHERE rowid = ?"
    #     self.c.execute(sql_load, (self.watch_id,))
    #     data = self.c.fetchone()
    #
    #     self.watch_name = data['watch_name']
    #     self.notes = data['notes']
    #     self.total_alarms = data['total_alarms']
    #     self.run_next_alarm_immediately = data['run_next_alarm_immediately']
    #     self.watch_id = data['watch_id']
    #     self.was_last_opened = data['was_last_opened']
    #
    # def make_data(self):
    #     self.c.execute("""INSERT INTO watches(watch_name, notes, total_alarms, run_next_alarm_immediately, watch_id, was_last_opened)
    #                        VALUES (?, ?, ?, ?, ?, ?)""", (self.prepareData()))
    #     # self.alarm_id = self.c.lastrowid
    #     self.conn.commit()
    #     self.load_data()
    #
    # def update_data(self):
    #     data = self.prepareData()
    #     data.append(self.watch_id)
    #
    #     sql_update = ('''\
    #             UPDATE watches SET watch_name = :value1, notes = :value2, total_alarms = :value3, run_next_alarm_immediately = :value4,
    #             watch_id = :value5, was_last_opened = :value6
    #             WHERE rowid = ?
    #             ''')
    #     self.c.execute(sql_update, data)
    #     # self.c.execute("UPDATE alarms SET positionx = positiony = name = beginning_time = remaining_time = "
    #     #              "is_time_specific_checked = notify_dropdown_time = specific_notify_time = alarm_sound = watch_id = ) "
    #     #             "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.prepareData()))
    #     self.conn.commit()
    #     # self.c.execute("SELECT * FROM alarms")
    #     # stuff = self.c.fetchall()
    #     # for things in stuff:
    #     #     for thing in things:
    #     #         print(thing)
    #     #     print(things)
    #
    # def prepareData(self):
    #     prepared_data = []
    #     dictionary = {
    #         'watch_name': self.watch_name,
    #         'notes': self.notes,
    #         'total_alarms': self.total_alarms,
    #         'run_next_alarm_immediately': self.run_next_alarm_immediately,
    #         'watch_id': self.watch_id,
    #         'was_last_opened': self.was_last_opened
    #     }
    #     for data in dictionary:
    #         prepared_data.append(dictionary[data])
    #     return prepared_data
    #
    # def getInsideWatchFrame(self):
    #     return self.inside_watch
    #
    # def close(self):
    #     print("close")
    #     self.inside_watch.grid_remove()
    #     self.watch_name_button.grid_remove()
    #     self.watch_settings_button.grid_remove()
    #     self.watch_name_button = Button(self.frame_of_watches, text=self.watch_name, width=23, anchor=W,
    #                                     command=self.watch_clicked)
    #     self.watch_settings_button = Button(self.frame_of_watches, text=":", command=self.open_watch_settings)
    #     self.watch_name_button.grid(row=self.watch_id, column=0)
    #     self.watch_settings_button.grid(row=self.watch_id, column=1)
    #     self.was_last_opened = 0
    #     # self.c.execute("UPDATE awatches SET is_on = 'off' WHERE rowid = self.watch_id")
    #     # self.frame_of_watches.grid_remove()
