import win32print
import win32ui
import win32con
import win32gui

file = "docs/sample.pdf"
content  =  "Hello world!"#"Chương Hòa Lộc"

# get printer default
printer_name = win32print.GetDefaultPrinter()
print(printer_name)

# define print defaults
printdefaults = {"DesiredAccess":win32print.PRINTER_ACCESS_USE};
handle = win32print.OpenPrinter(printer_name,printdefaults)
print(handle)

# attribute
level = 2 # 2 = error
attributes = win32print.GetPrinter(handle,level)

# get rect
rect = (0,0,200,200)#win32gui.GetClientRect(hWnd) (left, top, right, bottom) form (0,0) to starting drawing point (200,200)

hDC = win32ui.CreateDC() # Creates a PyCDC object.  A Device Context. Encapsulates an MFC CDC class.
hDC.CreatePrinterDC(win32print.GetDefaultPrinter()) # Creates a device context for a specific printer 
hDC.StartDoc("Test doc") # Starts spooling a document to a printer DC 
hDC.StartPage() # Starts a new page on a printer DC
hDC.SetMapMode(win32con.MM_TEXT)
hDC.DrawText(content,rect,win32con.DT_CENTER)
hDC.EndPage()
hDC.EndDoc()

