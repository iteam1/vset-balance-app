import win32print 
import win32ui
import time
import requests
import json
import code128
import io
from PIL import Image,ImageWin,ImageDraw,ImageFont

class printer():
    def __init__(self):
        self.IMAGE_WIDTH = 670 # pixel
        self.IMAGE_HEIGHT = 160 # pixel
        self.OFFSET_X_PIXEL = 0 # offset x position
        self.OFFSET_Y_PIXEL = 0 # offset y position
        self.SCALE_SIZE = 0.5 # scale factor
        self.barcode_path = "./barcode"
        self.printer_name = win32print.GetDefaultPrinter() # get printer default
        self.fnt = ImageFont.truetype('./segoe-ui/SEGOEUIB.TTF', 15) # create font
        self.shape = [(0,0),(670,0),(670,160),(0,160),(0,0)]
        self.hDC= win32ui.CreateDC()
        self.hDC.CreatePrinterDC(self.printer_name)
        
    def generate_img(self,img_name,barcode_content="12345678"):
        # INIT PILLOW IMAGE
        img = Image.new('RGB',(self.IMAGE_WIDTH,self.IMAGE_HEIGHT),color = 'white')
        d = ImageDraw.Draw(img)
        #DRAW SHAPE
        d.line(self.shape,fill = "black",width=5)
        d.line([(self.IMAGE_WIDTH/2,0),(self.IMAGE_WIDTH/2,self.IMAGE_HEIGHT)],fill = "black",width=3)
        # BARCODE
        barcode_image = code128.image(barcode_content, height=80)
        img.paste(barcode_image,(355,80))
        # TEXT PAGE1
        d.text((10,10),"XIN CHÀO DÒNG 1!",font = self.fnt,fill=(0,0,0))
        d.text((10,40),"XIN CHÀO DÒNG 2!",font = self.fnt,fill=(0,0,0))
        d.text((10,70),"XIN CHÀO DÒNG 3!",font = self.fnt,fill=(0,0,0))
        d.text((10,100),"XIN CHÀO DÒNG 4!",font = self.fnt,fill=(0,0,0))
        # TEXT PAGE2
        d.text((400,10),"XIN CHÀO DÒNG 1!",font = self.fnt,fill=(0,0,0))
        d.text((400,40),"XIN CHÀO DÒNG 2!",font = self.fnt,fill=(0,0,0))
        
        img.save(f"{self.barcode_path}/{img_name}.png")
    
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
barcode_list = list(tasks_printer.keys())
#print(barcode_list)

#Generate image
thermal_printer.generate_img(barcode_list[0])
#Print

# Clear all barcode

#Delay