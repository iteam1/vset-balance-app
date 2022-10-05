import win32print 
import win32ui
import requests
import json
import time
import code128
import io
import os
from PIL import Image,ImageWin,ImageDraw,ImageFont,ImageOps

class printer():
    def __init__(self):
        self.IMAGE_WIDTH = 670 # pixel
        self.IMAGE_HEIGHT = 160 # pixel
        self.OFFSET_X_PIXEL = 0 # offset x position
        self.OFFSET_Y_PIXEL = 0 # offset y position
        self.SCALE_SIZE = 0.5 # scale factor
        self.barcode_path = "./barcode"
        self.printer_name = win32print.GetDefaultPrinter() # get printer default
        self.fnt = ImageFont.truetype('./segoe-ui/SEGOEUIB.TTF', 22) # create font
        self.shape = [(0,0),(670,0),(670,160),(0,160),(0,0)]
        self.hDC= win32ui.CreateDC()
        self.hDC.CreatePrinterDC(self.printer_name)
    
    def generate_img(self,img_name,page1,page2,other,shape = False):
        # INIT PILLOW IMAGE
        img = Image.new('RGB',(self.IMAGE_WIDTH,self.IMAGE_HEIGHT),color = 'white')
        text_layer = Image.new('L',(160,30))
        d = ImageDraw.Draw(img)
        d_text = ImageDraw.Draw(text_layer)
        # DRAW TEXT OTHER
        d_text.text((0,0),other,font = ImageFont.truetype('./segoe-ui/SEGOEUIB.TTF', 20),fill="white")
        rotated_text_layer = text_layer.rotate(-90,expand=1)
        #rotated_text_layer.show()
        img.paste(ImageOps.colorize(rotated_text_layer,(0,0,0),(10,10,10)),(305,7),rotated_text_layer)
        # DRAW SHAPE
        if shape:
            d.line(self.shape,fill = "black",width=3)
            d.line([(self.IMAGE_WIDTH/2,0),(self.IMAGE_WIDTH/2,self.IMAGE_HEIGHT)],fill = "black",width=3)
        # BARCODE
        barcode_content=page2['barcode']
        barcode_image = code128.image(barcode_content, height=40)
        img.paste(barcode_image,(355,80))
        # TEXT BARCODE
        d.text((460,120),barcode_content,font = self.fnt,fill=(0,0,0))
        # TEXT PAGE1
        d.text((10,10),page1,font = self.fnt,fill=(0,0,0))
        # d.text((10,40),"XIN CHÀO DÒNG 2!",font = self.fnt,fill=(0,0,0))
        # d.text((10,70),"XIN CHÀO DÒNG 3!",font = self.fnt,fill=(0,0,0))
        # d.text((10,100),"XIN CHÀO DÒNG 4!",font = self.fnt,fill=(0,0,0))
        # TEXT PAGE2
        d.text((400,10),page2['text'],font = self.fnt,fill=(0,0,0))
        # d.text((400,40),"XIN CHÀO DÒNG 2!",font = self.fnt,fill=(0,0,0))
        # SAVE IMAGE
        img.save(f"{self.barcode_path}/{img_name}.png")
    
    def print_barcode(self,file):
        bmp = Image.open(file) # open image convert to bitmap
        self.hDC.StartDoc(file)
        self.hDC.StartPage()
        dib = ImageWin.Dib(bmp)
        scaled_width,scaled_height = [int(self.SCALE_SIZE * i) for i in bmp.size] # resize width to width scale,height to height scale
        # calculate (top,left,bottom,right)
        x1 = 0 + self.OFFSET_X_PIXEL
        y1 = 0 + self.OFFSET_Y_PIXEL
        x2 = x1 + scaled_width
        y2 = y1 + scaled_height
        # Magic command
        dib.draw(self.hDC.GetHandleOutput(),(x1,y1,x2,y2))
        self.hDC.EndPage()
        self.hDC.EndDoc()
        #self.hDC.DeleteDC()

# Init
base_url = 'https://gold-pos.vvs.vn/parse/classes/PrintJob'
headers = {"X-Parse-Application-Id":"SCWASRTWK1Y9AVMP1KFC",}

delete_base_url = 'https://gold-pos.vvs.vn/parse/classes/PrintJob/D9UrWx2m0H'
delete_headers = {"X-Parse-Application-Id":"SCWASRTWK1Y9AVMP1KFC"}

file_path = "./docs/json_api.json"
thermal_printer = printer()

# Loop

#Send request and Load json
# with requests.Session() as s:
#     res = s.get(base_url,headers=headers)
# tasks = res.json()
with open(file_path,'r') as f:
    tasks = json.load(f)
    
#print(tasks)

print(f"Printing: {len(tasks['results'])} stamps")

#Generate image
print(f"Generating: {len(tasks['results'])} stamps")
for i in range(len(tasks['results'])):
    stamp = tasks['results'][i]
    objectId = stamp['objectId']
    page1 = stamp['page1']
    page2 = stamp['page2']
    other = stamp['other']
    thermal_printer.generate_img(objectId,page1,page2,other,shape = True) #

# Print byThermal printer
# for i in range(len(tasks['results'])):
#     stamp = tasks['results'][i]
#     objectId = stamp['objectId']
#     file_name = f"{thermal_printer.barcode_path}/{objectId}.png"
#     print("Printing: ",file_name)
#     try:
#         thermal_printer.print_barcode(file_name)
#     except:
#         print("Can NOT print: ",file_name)
#         pass # go to next item
#     time.sleep(1)

# Clear API
# for i in range(len(tasks['results'])):
#     stamp = tasks['results'][i]
#     objectId = stamp['objectId']
#     delete_base_url = 'https://gold-pos.vvs.vn/parse/classes/PrintJob/{objectId}'
#     with requests.Session() as s:
#         res = s.delete(delete_base_url,headers=delete_headers)
#     print(f"Deleted : {objectId} on server")

# Clear all barcode in floder
# print(f"Deleting Image: {len(tasks['results'])} stamps")
# for i in range(len(tasks['results'])):
#     stamp = tasks['results'][i]
#     objectId = stamp['objectId']
#     os.remove(f"{thermal_printer.barcode_path}/{objectId}.png")
    
#Delay
# time.sleep(5)
# os.system('cls')
    