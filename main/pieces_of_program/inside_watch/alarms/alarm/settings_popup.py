from tkinter import *
from ....database import alarms
def render(current_alarm, app):
    global notify_dropdown
    if current_alarm.alarm_clock.stop == False:
        current_alarm.pause()
    settings_window = Toplevel()
    settings_window.config(bg=app.third_bg_color)
    settings_window.iconbitmap("../Images/Stopwatch Time Manager.ico")

    labels_frame = LabelFrame(settings_window, bg=app.third_bg_color, borderwidth=5)
    labels_frame.grid(row=0, column=0)

    set_settings_frame = LabelFrame(settings_window, bg=app.alarm_labels_color, borderwidth=5)
    set_settings_frame.grid(row=0, column=1)

    label1 = Label(labels_frame, text="Change the alarm time.", bg=app.third_bg_color)
    label1.grid(row=0, column=0)


    # Settings for changing alarm time
    timevar = StringVar(settings_window)
    timevar.set(current_alarm.alarm_clock.initial_time)

    time_entry = Entry(set_settings_frame, textvariable=timevar, bg=app.entry_bg_color)
    time_entry.grid(row=0, column=3, columnspan=2)

    # Settings for changing notifications

    notify_question= Label(labels_frame, text="When do you want to receive a notification regarding your alarm?\n"
                                                 "(Select None if you don't want any.)", bg=app.third_bg_color)
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

    notify_dropdown = OptionMenu(set_settings_frame, notify_time, *time_increment_options)
    notify_dropdown.grid(row=1, column=3, columnspan=2)
    notify_dropdown.config(bg=app.button_main_color)
    notify_dropdown['menu'].config(bg=app.button_main_color)

    # For using specific times for the time increment notifications

    use_specific_time_label = Label(labels_frame, text="      Use a specific time other than the ones listed?\n"
                                                          "      (Note the time must be in the format 'x:xx:xx.'')",
                                     bg=app.third_bg_color)
    use_specific_time_label.grid(row=1, column=1)

    notify_time_specific = StringVar()
    notify_time_specific.set("None")

    def checkbox_action():
        global notify_dropdown
        global notify_entry
        if specific_time_choice.get() == 0:
            notify_dropdown.grid_forget()
            notify_dropdown = OptionMenu(set_settings_frame, notify_time, *time_increment_options)
            notify_dropdown.grid(row=1, column=3, columnspan=2)
            notify_dropdown.config(bg=app.button_main_color)
            notify_dropdown['menu'].config(bg=app.button_main_color)
            notify_time_specific.set("None")
            notify_entry.grid_forget()
        else:
            notify_dropdown.grid_forget()
            notify_entry = Entry(set_settings_frame, textvariable=notify_time_specific, bg=app.entry_bg_color)
            notify_entry.grid(row=1, column=4)

    specific_time_choice = IntVar()
    specific_time_choice.set(0)
    specific_time_checkbox = Checkbutton(set_settings_frame, variable=specific_time_choice,
                                         command=checkbox_action, bg=app.button_main_color)
    specific_time_checkbox.grid(row=1, column=2)


    # Asking what sound do you want when your alarm goes off.

    asking_alarm_sound = Label(labels_frame, text="What sound do you want to play when your alarm goes off?", bg=app.third_bg_color)
    asking_alarm_sound.grid(row=2, column=0)

    sound_options = [
        "Classic Alarm",
        "Kitchen Alarm",
        "Tall-Case/Grandfather Clock Alarm",
    ]

    alarm_sound_tk_var = StringVar(settings_window)
    alarm_sound_tk_var.set(sound_options[0])

    alarm_sound_dropdown = OptionMenu(set_settings_frame, alarm_sound_tk_var, *sound_options)
    alarm_sound_dropdown.grid(row=2, column=3, columnspan=2)
    alarm_sound_dropdown.config(bg=app.button_main_color)
    alarm_sound_dropdown['menu'].config(bg=app.button_main_color)


    save_button = Button(set_settings_frame, text="Save Settings", command=lambda: save_settings(current_alarm,
                        timevar.get(), specific_time_choice.get(), notify_time_specific.get(), notify_time.get(),
                                                                                              alarm_sound_tk_var.get()),
                         bg=app.button_main_color)
    save_button.grid(row=6, column=3, columnspan=2)


    def save_settings(current_alarm, new_time, is_specific_time_checked, new_notify_time_specific, new_notify_time,
                      new_alarm_sound):

        # current_alarm.remaining_time = new_time
        # current_alarm.beginning_time = new_time

        current_alarm.is_specific_time_checked = is_specific_time_checked

        current_alarm.alarm_clock.initial_time = new_time
        current_alarm.alarm_clock.remaining_time = new_time

        current_alarm.alarm_clock.digital.config(text=new_time)
        current_alarm.notify_time_specific = new_notify_time_specific
        current_alarm.notify_time = new_notify_time
        current_alarm.alarm_sound = new_alarm_sound

        prepared_data = current_alarm.get_prepared_data()
        prepared_data.append(current_alarm.alarm_id)
        alarms.update_alarm(prepared_data)
        if current_alarm.reset_button.button['state'] == NORMAL:
            current_alarm.reset()

        settings_window.destroy()

