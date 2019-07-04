import sys
from tqdm import tqdm
from PyPDF2 import PdfFileReader

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
        
        # The password is of the format : "1051-0981-XXXXXX-01-8" , where "XXXXXX" is a 6 digit unknown number.
        
        a = str("1051-0981-" + str(z) + "-01-8")
               
        if pdffile.decrypt(a) > 0:
                print ("[+] Password is: " + a)
                print ("[...] Exiting..")
                sys.exit()