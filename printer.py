import win32print
import sys
from pathlib import Path

# Python 3 only..
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

printers = win32print.EnumPrinters(4)
printercount = 0
for x in printers:
    print(printercount, "-", x[2])
    printercount += 1

chosenprinter = int(input("Printer number? "))

chosenfile = Path()
while not chosenfile.is_file():
    filename = input("Enter PDF file path: ")
    chosenfile = Path(filename)

myprinter = win32print.OpenPrinter(printers[chosenprinter][2])

printjob = win32print.StartDocPrinter(
    myprinter, 1, ("Python test RAW print", None, "raw"))

with open(chosenfile, mode='rb') as file:
    buf = file.read()

bytesprinted = win32print.WritePrinter(myprinter, buf)

win32print.EndDocPrinter(myprinter)
win32print.ClosePrinter(myprinter)