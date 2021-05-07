from tkinter import *
def make_notes(watch_frame):
    notev = StringVar(watch_frame)
    notev.set("Edit notes here.")
    notes = LabelFrame(watch_frame)
    notes.grid(row=2, column=0)
    notetop = Label(notes, text="Notes", width=50, anchor=W)
    notetop.grid(row=0, column=0)
    noteentry = Entry(notes, width=44, textvariable=notev)
    noteentry.grid(row=1, column=0)
    buttonsave = Button(notes, text="Save notes", command=lambda: print("Need to add saving notes ability"))
    buttonsave.grid(row=2, column=0)