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
        self.hDC= win32ui.CreateDC()
        self.hDC.CreatePrinterDC(self.printer_name)
    
    def print_barcode(self,file):
        bmp = Image.open(file) # open image convert to bitmap
        
        self.hDC.StartDoc("Test img")
        self.hDC.StartPage()
        
        dib = ImageWin.Dib(bmp)

        scaled_width,scaled_height = [int(self.SCALE_SIZE * i) for i in bmp.size] # resize width to width scale,height to height scale
        
        # calculate (top,left,bottom,right)
        x1 = 0 + OFFSET_X_PIXEL
        y1 = 0 + OFFSET_Y_PIXEL
        x2 = x1 + scaled_width
        y2 = y1 + scaled_height
        
        # Magic command
        dib.draw(self.hDC.GetHandleOutput(),(x1,y1,x2,y2))

        self.hDC.EndPage()
        self.hDC.EndDoc()
        self.hDC.DeleteDC()

# Init
file_path = "./docs/task_printer.json"
thermal_printer = printer()

# Loop

#Send request and Load json
f = open(file_path) # read text
tasks_printer = json.load(f) # convert text to json
#print(tasks_printer)

#Generate image

#Print

#Delay