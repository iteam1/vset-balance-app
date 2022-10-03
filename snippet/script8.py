import win32print

content = '''hello'''

p = win32print.OpenPrinter(win32print.GetDefaultPrinter())

job = win32print.StartDocPrinter(p,1, ("Test Raw", None, "RAW"))

win32print.StartPagePrinter(p)

win32print.WritePrinter(p,bytes("Print Me Puhleeezzz!","utf-8")) # content.encode("utf8")

win32print.EndPagePrinter(p)

win32print.EndDocPrinter(p)

win32print.ClosePrinter(p)