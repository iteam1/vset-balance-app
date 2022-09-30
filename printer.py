import os, sys
import win32print

printer_name = win32print.GetDefaultPrinter()
#
# raw_data could equally be raw PCL/PS read from
#  some print-to-file operation
#

if sys.version_info >= (3,):
  raw_data = bytes ("This is a test", "utf-8")
else:
  raw_data = "This is a test"

hPrinter = win32print.OpenPrinter (printer_name)
try:
  hJob = win32print.StartDocPrinter (hPrinter, 1, ("test of raw data", None, "RAW"))
  try:
    win32print.StartPagePrinter (hPrinter)
    win32print.WritePrinter (hPrinter, raw_data)
    win32print.EndPagePrinter (hPrinter)
  finally:
    win32print.EndDocPrinter (hPrinter)
finally:
  win32print.ClosePrinter (hPrinter)
