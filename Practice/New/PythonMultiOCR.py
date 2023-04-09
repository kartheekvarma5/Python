from PIL import Image
from pytesseract import pytesseract

TesseractPath = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
AllImages = str(input("Please Input the file name : "))


'''
for IMG in AllImages:
    #ImageOCROutFile = IMG.replace('JPG','txt').replace('PNG','txt').replace('gif','txt')
    #OpenIMG = Image.open(IMG)
    #pytesseract.tesseract_cmd = TesseractPath
    #ExtractedText = pytesseract.image_to_string(OpenIMG)
    #FileOperatons = open(ImageOCROutFile, "x")
    #FileOperatons.write(ExtractedText)
    #FileOperatons.close()
    #print("File", ImageOCROutFile, "Has been created in current directory")
    print(IMG)
    
#Above script is not working
'''
