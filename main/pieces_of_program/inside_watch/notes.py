from tkinter import *
def render(app, watch_frame):
    notev = StringVar(watch_frame)
    notev.set("Edit notes here.")
    notes = LabelFrame(watch_frame, bg=app.third_bg_color)
    notes.grid(row=2, column=0)
    notetop = Label(notes, text="Notes", width=50, anchor=W, bg=app.alarm_labels_color)
    notetop.grid(row=0, column=0, columnspan=2)
    noteentry = Entry(notes, width=44, textvariable=notev, bg=app.entry_bg_color)
    noteentry.grid(row=1, column=0, pady=8)
    buttonsave = Button(notes, text="Save notes", command=lambda: print("Need to add saving notes ability"),
                        bg=app.button_main_color)
    buttonsave.grid(row=2, column=1)