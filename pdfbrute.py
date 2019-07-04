import sys
import datetime 
from tqdm import tqdm
from PyPDF2 import PdfFileReader

print (datetime.datetime.now())

pdffile = PdfFileReader("statement.pdf", "rb")
if pdffile.isEncrypted == False:
        print ("[!] The file is not protected with any password. Exiting.")
        exit

print ("[+] Attempting to Brute force. This will take time...")

z = ""
for i in tqdm(range(999999, 0, -1)):
        z = str (i)
        while (len(z) < 6):
                z = "0" + z
        
        a = str("1051-0981-" + str(z) + "-01-8")
               
        if pdffile.decrypt(a) > 0:
                print ("[+] Password is: " + a)
                print ("[...] Exiting..")
                sys.exit()