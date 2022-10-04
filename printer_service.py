import win32print 
import win32ui
import time
import json
from PIL import Image,ImageWin

class printer():
    def __init__(self):
        self.OFFSET_X_PIXEL = 0 # offset x position
        self.OFFSET_Y_PIXEL = 0 # offset y position
        self.SCALE_SIZE = 0.5 # scale factor
        self.printer_name = win32print.GetDefaultPrinter() # get printer default

# Init
file_path = "./docs/task_printer.json"

# Loop

#Send request and Load json
f = open(file_path) # read text
tasks_printer = json.load(f) # convert text to json
#print(tasks_printer)

#Generate image

#Print

#Delay