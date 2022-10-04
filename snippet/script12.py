import win32print 
import win32ui
from PIL import Image,ImageWin

'''
template width  670px  = 42cm
template height 160px <= 10cm
'''
file_path = "docs/template2.PNG"

OFFSET_X_PIXEL = 0 # offset x position
OFFSET_Y_PIXEL = 0 # offset y position
SCALE_SIZE = 0.5 # scale factor

# get printer default
printer_name = win32print.GetDefaultPrinter()
print(f"Default Printer (thermal printer) {printer_name}")

hDC= win32ui.CreateDC()
hDC.CreatePrinterDC(printer_name)

bmp = Image.open(file_path)
print(f"bmp size [{bmp.size[0]},{bmp.size[1]}]")

hDC.StartDoc("Test img")
hDC.StartPage()
dib = ImageWin.Dib(bmp)

scaled_width,scaled_height = [int(SCALE_SIZE * i) for i in bmp.size] # resize width to width scale,height to height scale
print(f"scaled_img size: {scaled_width},{scaled_height}")

x1 = 0 + OFFSET_X_PIXEL
y1 = 0 + OFFSET_Y_PIXEL
x2 = x1 + scaled_width
y2 = y1 + scaled_height

print(f"(x1,y1,x2,y2) = ({x1},{y1},{x2},{y2})")

# Magic command
dib.draw(hDC.GetHandleOutput(),(x1,y1,x2,y2))

hDC.EndPage()
hDC.EndDoc()
hDC.DeleteDC()