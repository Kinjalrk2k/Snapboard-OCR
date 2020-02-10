import pyperclip
import pytesseract
from PIL import ImageGrab
from PIL import Image  #Image is required to load input image in PIL format
import pytesseract     #pytesseract is used to recognise the text from image 

def run_ocr(image_file):
    pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # specifying the path to the tesseract.exe file
    img = Image.open(image_file) # accessing the image 
    output_text = pytesseract.image_to_string(img, lang= 'eng') # converting the image contents to string
    # print(output_text) # printing the image contents in terminal
    return output_text

image_file = 'snap.png'

img = ImageGrab.grabclipboard()
img.save(image_file,'PNG')

text = run_ocr(image_file)

pyperclip.copy(text)

print(text)

