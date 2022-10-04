import win32print 
import win32ui
from PIL import Image,ImageWin

file_path = "docs/barcode.PNG"

# Constants for GetDeviceCaps
# HORZRES / VERTRES = printable area
HORZRES = 8
VERTRES = 10

# LOGPIXELS = dots per inch
LOGPIXELSX = 88
LOGPIXELSY = 90

# PHYSICALWIDTH/HEIGHT = total area
PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111

# PHYSICALOFFSETX/Y = left / top margin
PHYSICALOFFSETX =112
PHYSICALOFFSETY = 113

# get printer default
printer_name = win32print.GetDefaultPrinter()
print(f"Default Printer (thermal printer) {printer_name}")

# You can only write a Device-independent bitmap
#  directly to a Windows device context; therefore
#  we need (for ease) to use the Python Imaging
#  Library to manipulate the image.
#
# Create a device context from a named printer
#  and assess the printable size of the paper.

hDC= win32ui.CreateDC()
hDC.CreatePrinterDC(printer_name)
printable_area = (hDC.GetDeviceCaps(HORZRES),hDC.GetDeviceCaps(VERTRES)) # tuple
print(f"printable_area: {printable_area}")
printer_size = (hDC.GetDeviceCaps(PHYSICALWIDTH),hDC.GetDeviceCaps(PHYSICALHEIGHT))
print(f"printer_size: {printer_size}")
printer_margins = (hDC.GetDeviceCaps(PHYSICALOFFSETX),hDC.GetDeviceCaps(PHYSICALOFFSETY))
print(f"printer_margins: {printer_margins}")

# Open the image, rotate it if it's wider than
#  it is high, and work out how much to multiply
#  each pixel by to get it as big as possible on
#  the page without distorting.
bmp = Image.open(file_path)
print(f"bmp size [{bmp.size[0]},{bmp.size[1]}]")
# if bmp.size[0] > bmp.size[1]:
#     bmp = bmp.rotate(90)
    
ratios = [1.0 * printable_area[0] / bmp.size[0] , 1.0 * printable_area[1] / bmp.size[1]]
print(f"ratios: {ratios}")
scale = min(ratios)
print(f"scale: {scale}")

# Start the print job, and draw the bitmap to
#  the printer device at the scaled size.
hDC.StartDoc("Test img")
hDC.StartPage()
dib = ImageWin.Dib(bmp)
scaled_width,scaled_height = [int(scale * i) for i in bmp.size] # resize width to width scale,height to height scale
print(f"scaled_img size: {scaled_width},{scaled_height}")
x1 = int((printer_size[0] - scaled_width)/2)
y1 = int((printer_size[1] - scaled_height)/2)
x2 = x1 + scaled_width
y2 = y1 + scaled_height
print(f"(x1,y1,x2,y2) = ({x1},{y1},{x2},{y2})")

# Magic command
dib.draw(hDC.GetHandleOutput(),(x1,y1,x2,y2))

hDC.EndPage()
hDC.EndDoc()
hDC.DeleteDC()