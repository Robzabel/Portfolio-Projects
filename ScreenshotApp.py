import time, pyautogui
from datetime import datetime
import tkinter as tk

def screenshot():

    d_t = datetime.now()                                                            # Get the current date and time for the screenshot name, save it in a variable
    name = '/home/zabex/PythonProjects/ScreenCaptures/{}.png'.format(d_t)           # use an in-line format string to create the date and time naming variable
    img = pyautogui.screenshot( name)                                               # use the name variable and attach a file format
    img.show()                                                                      # preview the image

root = tk.Tk()                                                                      # create the gui window frame
frame = tk.Frame(root)
frame.pack()

Snap = tk.Button(                                                                   # create the first button
    frame,                                                                          # put it in the root frame
    text = 'Take Snap',                                                             # give the button some descriptive text
    command = screenshot)                                                           # tell the button what to do
Snap.pack(side=tk.LEFT)                                                             # set the packing for the button in the frame

close = tk.Button(
    frame, 
    text = 'Quit',                                                                  # same as the Snap button but for exiting the programme
    command = quit)
close.pack(side=tk.LEFT)

root.mainloop()                                                                     # create the main loop which means you can press the button multiple times

