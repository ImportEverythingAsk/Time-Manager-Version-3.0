from tkinter import *
# Note ButtonObject is a better name for our file Buttonbox now that it's purpose kinda changed.
class ButtonObject(Button):
    buttonbox = ""
    button = ""
    current_image = ""
    def __init__(self, buttonbox, normal_image, disabled_image, default_state, command):
        self.buttonbox = buttonbox
        self.normal_image = normal_image
        self.disabled_image = disabled_image
        self.current_state = default_state
        self.command = command
        self.buttonbox.grid(row=2, column=0)

        if self.current_state == NORMAL:
            self.current_image = normal_image
        else:
            self.current_image = disabled_image

        self.button = Button(self.buttonbox, image=self.current_image, state=self.current_state, command=command)
    def toggle(self):
        if self.current_state == DISABLED:
            self.current_image = self.normal_image
            self.current_state = NORMAL
        else:
            self.current_image = self.disabled_image
            self.current_state = DISABLED
        self.button.config(image=self.current_image, state=self.current_state)
