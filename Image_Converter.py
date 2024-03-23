from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *

from PIL import Image

window = Tk()  # create a window.

window_width = 500
window_height = 350
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)

space = ' '
window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
window.title(space*40+'JPEG to PNG Convertor')


file = ''
new_window = None


def select_image():  # function of select image button

    global file
    # get path of selected image as string
    file = fd.askopenfilename(filetypes=(
        ('JPEG Files', '*.JPG'), ('All Files', '*.*')))

    global new_window
    new_window = Toplevel(window)  # creating new frame over root window
    new_window.geometry('500x350')
    Label(new_window, text=f'Selected File : {file}').pack()

    # adding button to new window to convert image.
    my_btn2 = Button(new_window, text='Convert', command=convert)
    my_btn2.pack()


def convert():  # functionality of convert button

    global file
    if file.endswith(('.jpg', '.JPG', '.jpeg', '.JPEG')):
        img = Image.open(file)
        exported_img = fd.asksaveasfilename(defaultextension='.png')
        img.save(exported_img)

        Label(new_window, text=f'Successfully Converted ! \n \n Saved to : {
              exported_img}').pack()

    else:
        Label(new_window, text='Please select a JPEG file').pack()


# Create a button to select image
my_btn = Button(window, text='Select your Image', command=select_image)
my_btn.pack()     # Display the button.
window.mainloop()  # Display the  window.
