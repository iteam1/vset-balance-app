# coding: utf8

import win32print

class ZPLLabel(object):
    def __init__(self, printerName):
        self.printerName = printerName
        self.printerDevice = win32print.OpenPrinter(self.printerName)
        self.job = win32print.StartDocPrinter(self.printerDevice, 1, ("Etiquette", None, "RAW"))
        self.eraseAll()
        self.defineFormat()

    def eraseAll(self):
        win32print.StartPagePrinter(self.printerDevice)
        str2print="~JA"
        win32print.WritePrinter(self.printerDevice, str2print.encode("utf8")) #écrit le format d'étiquette
        win32print.EndPagePrinter(self.printerDevice) # indique la fin de ce qu'il y a à imprimer
        self.printerDevice.close() # ferme le canal d'impression et déclenche l'impression de ce qui précède
        #del self.job    
        self.printerDevice=win32print.OpenPrinter(self.printerName)
        self.job = win32print.StartDocPrinter(self.printerDevice, 1, ("Etiquette", None, "RAW"))

    def defineFormat(self):
        margeLeft = 150
        margeTop = 20
        interLine = 39
        shiftLeft = 20
        vDec = 25
        #win32print.StartPagePrinter(p)
        str2print="^XA\n" #debut de format
        str2print+="^CI28"
        #FO origine du champ, 100 pos x du champ en dots, 50 pos y du champ en dots
        # l'imprimantes est 200 dpi (dotsper inch = 7.874 dots par mm, ici 12.7mm, 6.35mm)
        #ADN : A ==> font, D==> font D, N ==> Orientation Normale, 36 hauteur caractère en dots, 20 Largeur caractère en dots
        #FD données à imprimer pour le champ
        #FS fin du champ
        str2print+="^DFFORMAT"
        str2print+="^LH"+str(margeLeft)+","+str(margeTop)
        #un cadre arrondi
        str2print+="^FO0,0^GB500,330,3,B,2^FS"    
        #str2print+="^FO"+str(shiftLeft)+","+str(interLine)+"^ADN,24,12^FDEtiquette de débit Sangle^FS\n" #format de l'étiquette
        str2print+="^FO"+str(shiftLeft)+","+str(1*interLine-vDec) +"^ADN,32,14^FDOF N° : ^FS^FO"+str(shiftLeft+160)+","+str(1*interLine-vDec) +"^ADN,32,14^FN1^FS"
        str2print+="^FO"+str(shiftLeft)+","+str(2*interLine-vDec) +"^ADN,32,14^FDPRODUIT : ^FS^FO"+str(shiftLeft+215)+","+str(2*interLine-vDec) +"^ADN,32,14^FN2^FS"
        str2print+="^FO"+str(shiftLeft)+","+str(3*interLine-vDec) +"^ADN,24,12^FN3^FS"
        str2print+="^FO"+str(shiftLeft)+","+str(4*interLine-vDec) +"^ADN,32,14^FDSANGLE : ^FS^FO"+str(shiftLeft+200)+","+str(4*interLine-vDec) +"^ADN,32,14^FN4^FS"
        str2print+="^FO"+str(shiftLeft)+","+str(5*interLine-vDec) +"^ADN,24,12^FN5^FS"
        str2print+="^FO"+str(shiftLeft)+","+str(6*interLine-vDec) +"^ADN,28,13^FDNombre de coupe : ^FS^FO"+str(shiftLeft+250)+","+str(6*interLine-vDec) +"^ADN,28,13^FN6^FS"
        str2print+="^FO"+str(shiftLeft)+","+str(7*interLine-vDec) +"^ADN,28,13^FDLongueur coupée : ^FS^FO"+str(shiftLeft+250)+","+str(7*interLine-vDec) +"^ADN,28,13^FN7^FS"
        str2print+="^FO"+str(shiftLeft)+","+str(8*interLine-vDec) +"^ADN,24,12^FDEmplacement : ^FS^FO"+str(shiftLeft+160)+","+str(8*interLine-vDec) +"^ADN,24,12^FN8^FS"
        str2print+="^XZ" # fin du format d'étiquette
        win32print.WritePrinter(self.printerDevice, str2print.encode("utf8")) #écrit le format d'étiquette 

    def printLabel(self, orderNum, productSku, productName, webSku, webName, partNum, partLength, emplacement):
        str2print="^XA\n" #debut étiquette
        str2print+="^XFFORMAT" #rappel du format enregistré
        str2print+="^FN1^FD"+orderNum+"^FS"
        str2print+="^FN2^FD"+productSku+"^FS"
        str2print+="^FN3^FD"+productName+"^FS"
        str2print+="^FN4^FD"+webSku+"^FS"
        str2print+="^FN5^FD"+webName+"^FS"
        str2print+="^FN6^FD"+str(partNum)+"^FS"
        str2print+="^FN7^FD"+partLength+"^FS"
        str2print+="^FN8^FD"+emplacement+"^FS"
        str2print+="^XZ" # fin du format d'étiquette 
        win32print.WritePrinter(self.printerDevice, str2print.encode("utf8")) #écrit l'étiquette 

    def endLabel(self):
        self.printerDevice.close() # ferme le canal d'impression et déclenche l'impression de ce qui précède
        del self.job

def newPrintLabel():
    zpl = ZPLLabel(printerName = "Xprinter XP-350B")
    zpl.printLabel("20009999", "1035691", "Harnais Energy TWIN ss porte outil L/XL",
                       "90008318", "SA/SANGLE NOIRE 20 MM", 35, "0.38m", "Bavaroise réglable")
    zpl.endLabel()

if __name__ == '__main__':
    app = newPrintLabel()