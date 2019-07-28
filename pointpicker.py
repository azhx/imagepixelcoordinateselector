import json
import tkinter
import argparse
import PIL.Image
import PIL.ImageTk
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#  written by Alex Zhuang zhual@utschools.ca 2019/07/27

global out, t, second
PATH = str(input('relative path to img: '))

def output():
    """
    writes out the output json
    """
    top.destroy()

def delete():
    global second#, canvas, point
    """
    cancels the creation of a point by removing the red point
    """
    #canvas.delete(point)
    second.destroy()


def clicked(event):

    global index, lat, long, second, t, point
    if (event.x >= 0 and event.x <= photo.width() and event.y >= 0
            and event.y <= photo.height()):
        second = tkinter.Toplevel(width=300)

        x, y = (event.x), (event.y)
 
        second.grab_set()
        second.title("New Label")

        # message box
        msg = tkinter.Message(second, justify='center', width=300,
                              text="coords (x, y)")
        msg.pack()
        t = tkinter.Text(second, height=1, width=20)
        t.insert(1.0, f"{x, y}")
        t.pack()

        second.protocol("WM_DELETE_WINDOW", delete)
        second.mainloop()

# Create tk instance and set it to output the json on window close.
top = tkinter.Tk()
top.protocol("WM_DELETE_WINDOW", output)

# Open the map image and fit the window to the image dims
img = PIL.Image.open(PATH)
photo = PIL.ImageTk.PhotoImage(img)
top.geometry('{}x{}'.format(photo.width(), photo.height()))

# Place a canvas over the entire window
canvas = tkinter.Canvas(top, width=photo.width(), height=photo.height())
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
canvas.pack()

# on left-click on canvas, label a point
canvas.bind("<Button-1>", clicked)

top.mainloop()
