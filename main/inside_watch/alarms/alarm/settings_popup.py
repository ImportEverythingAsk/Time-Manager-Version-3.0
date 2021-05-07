from tkinter import *
def open_settings_popup():
    settings_window = Toplevel()
    settings_window.iconbitmap("../Images/Stopwatch Time Manager.ico")

    label1 = Label(settings_window, text="Change the alarm time.")
    label1.grid(row=0, column=0)


    # Settings for changing alarm time
    timevar = StringVar(settings_window)
    timevar.set("0:00:05")

    time_entry = Entry(settings_window, textvariable=timevar)
    time_entry.grid(row=0, column=3, columnspan=2)

    # Settings for changing notifications

    notify_question= Label(settings_window, text="When do you want to receive a notification regarding your alarm?\n"
                                                 "(Select None if you don't want any.)")
    notify_question.grid(row=1, column=0)


    time_increment_options = [
        "None",
        "1 minute",
        "2 minutes",
        "3 minutes",
        "5 minutes",
        "10 minutes",
        "15 minutes",
        "20 minutes",
        "30 minutes",
        "45 minutes",
        "60 minutes",
        "1 hour",
        "1 hour and 30 minutes",
        "2 hours"
    ]

    notify_time = StringVar(settings_window)
    notify_time.set(time_increment_options[0])

    notify_dropdown = OptionMenu(settings_window, notify_time, *time_increment_options)
    notify_dropdown.grid(row=1, column=3, columnspan=2)

    # For using specific times for the time increment notifications

    use_specific_time_label = Label(settings_window, text="      Use a specific time other than the ones listed?\n"
                                                          "      (Note the time must be in the format 'x:xx:xx.'')")
    use_specific_time_label.grid(row=1, column=1)

    notify_time_specific = StringVar()
    notify_time_specific.set("None")


    def checkbox_action():
        global notify_entry
        global notify_dropdown
        if specific_time_choice.get() == 0:
            is_specific_time_checked = 0
            notify_dropdown = OptionMenu(settings_window, notify_time, *time_increment_options)
            notify_dropdown.grid(row=1, column=3, columnspan=2)
            notify_time_specific.set("None")
            notify_entry.grid_forget()
        else:
            is_specific_time_checked = 1
            notify_dropdown.grid_forget()
            notify_entry = Entry(settings_window, textvariable=notify_time_specific)
            notify_entry.grid(row=1, column=4)


    specific_time_choice = IntVar()
    specific_time_choice.set(0)
    specific_time_checkbox = Checkbutton(settings_window, variable=specific_time_choice, command=checkbox_action)
    specific_time_checkbox.grid(row=1, column=2)

    # Asking what sound do you want when your alarm goes off.

    asking_alarm_sound = Label(settings_window, text="What sound do you want to play when your alarm goes off?")
    asking_alarm_sound.grid(row=2, column=0)

    sound_options = [
        "Classic Alarm",
        "Kitchen Alarm",
        "Tall-Case/Grandfather Clock Alarm",
    ]

    alarm_sound_tk_var = StringVar(settings_window)
    alarm_sound_tk_var.set(sound_options[0])

    alarm_sound_dropdown = OptionMenu(settings_window, alarm_sound_tk_var, *sound_options)
    alarm_sound_dropdown.grid(row=2, column=3, columnspan=2)


    save_button = Button(settings_window, text="Save Settings")
    save_button.grid(row=6, column=3, columnspan=2)
