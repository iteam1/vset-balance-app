import win32print

content = '''^XA
^CI28
^FO0,0^GB500,330,3,B,2^FS
^XZ'''

p = win32print.OpenPrinter(win32print.GetDefaultPrinter())

job = win32print.StartDocPrinter(p,1, ("Test Raw", None, "RAW"))

win32print.StartPagePrinter(p)

win32print.WritePrinter(p,content.encode("utf8")) # bytes("Print Me Puhleeezzz!","utf-8")

win32print.EndPagePrinter(p)

win32print.EndDocPrinter(p)

win32print.ClosePrinter(p)