
import pyqrcode

name = "parth Shukla\n"
Email = "parth.shukla@9ledgepro.com\n"
website = "shuklaparth.com"
Mobile_No = "9599587014\n"
LinkedID = "https://www.linkedin.com/in/parth-shukla-09205239/\n"
twitter = "https://twitter.com/parthshukl\n"

MyQR = pyqrcode.create(name+Email+website+Mobile_No+LinkedID+twitter)
MyQR.svg("MyQR.svg")

print("Your QRCode is ready to use, Flash it in Style.....")