from PIL import ImageTk,Image
def handle_images():
    global images
    global disabled_images
    global setting_image

    images = {}
    disabled_images = {}
    images["reset"] = ImageTk.PhotoImage(Image.open("../Images/Rewind.png"))
    images["play"] = ImageTk.PhotoImage(Image.open("../Images/Play_button.png"))
    images["pause"] = ImageTk.PhotoImage(Image.open("../Images/Pause_button.png"))
    setting_image = ImageTk.PhotoImage(Image.open("../Images/alarm.png"))

    disabled_images["reset"] = ImageTk.PhotoImage(Image.open("../Images/RewindDis.png"))
    disabled_images["play"] = ImageTk.PhotoImage(Image.open("../Images/PlayDis_Button.png"))
    disabled_images["pause"] = ImageTk.PhotoImage(Image.open("../Images/PauseDis_button.png"))
def give_images():
    return images, disabled_images, setting_image
