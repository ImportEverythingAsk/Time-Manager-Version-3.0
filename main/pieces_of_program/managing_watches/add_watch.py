from tkinter import *

def render(root):
    add_window = Toplevel()
    add_window.iconbitmap("../Images/Stopwatch Time Manager.ico")
    add_window.title("Add New Watch")

    global watch_name
    global total_alarms

    watch_name = StringVar()
    watch_name.set("Example: Go over yesterdays meeting")

    total_alarms = StringVar()
    total_alarms.set(0)

    name_question = Label(add_window, text="What do you want your watch to be called?")
    alarmsquestion = Label(add_window, text="How many alarms do you want? (Up to 18)")
    alarmsquestion.grid(row=2, column=0, columnspan=2)
    name_question.grid(row=0, column=0, columnspan=2)
    name_entry = Entry(add_window, textvariable=watch_name, width=40)
    name_entry.grid(row=1, column=0, columnspan=2)
    alarms_total_entry = Entry(add_window, textvariable=total_alarms, width=40)
    alarms_total_entry.grid(row=3, column=0, columnspan=2)
    cancel = Button(add_window, text="Cancel", command=add_window.destroy)
    cancel.grid(row=4, column=0)
    return add_window

def give_info():
    return watch_name.get(), total_alarms.get()