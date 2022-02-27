import pyqrcode
import png
data=input("Enter link or text for QR Code: ")
QRcode=pyqrcode.create(data)
name=input("Name of the QR Code: ")
QRcode.png(name+".png",scale=15) # For PNG format
QRcode.svg(name+".svg",scale=15) # For SVG format