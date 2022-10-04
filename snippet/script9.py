import win32print
import win32ui
import win32gui

file_path = "docs/sample.txt"
doc = open(file_path,'r').readlines() # return a list of sentences in document
print(doc)
f = 1

# get printer default
printer_name = win32print.GetDefaultPrinter()
print(f"Default Printer (thermal printer) {printer_name}")

hDC = win32ui.CreateDC()
hDC.CreatePrinterDC(win32print.GetDefaultPrinter())
hDC.StartDoc("Test doc")
hDC.StartPage()

for i,text in enumerate(doc):
    print(i,text)
    hDC.TextOut(0,i*f,text)
    hDC.MoveTo(0,i*f)

hDC.EndPage()
hDC.EndDoc()
