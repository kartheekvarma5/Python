from PIL import Image
from pytesseract import pytesseract
import smtplib

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = str(input("Please Input the file name : "))
out_file_name = image_path.replace('JPG','txt').replace('PNG','txt').replace('gif','txt')
img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
file = open(out_file_name, "x")
file.write(text)
file.close()
print("File", out_file_name, "Has been created in current directory")


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('rmgskumar@gmail.com', 'bednfhnlortq')
server.sendmail('rmgskumar@gmail.com', 'rmgskumar@gmail.com', 'TestMail')
#<Class>.<Method>(Object)
#<object>.<Method>  (Mostly we use this in all coding )
#Both Above works 