import pyperclip
import pytesseract
from PIL import ImageGrab
from PIL import Image  #Image is required to load input image in PIL format
import pytesseract     #pytesseract is used to recognise the text from image 
import imagehash
from win10toast import ToastNotifier


def run_ocr(image_file):
    pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # specifying the path to the tesseract.exe file
    img = Image.open(image_file) # accessing the image 
    output_text = pytesseract.image_to_string(img) # converting the image contents to string
    # print(output_text) # printing the image contents in terminal
    return output_text


def compare_img(im1, im2):
    if im1 == None or im2 == None:
        return False

    h1 = imagehash.average_hash(im1)
    h2 = imagehash.average_hash(im2)

    if abs(h1 - h2) == 0:
        return True  # images are same
    else:
        return False


def toast_notif(text):
    '''Toast a notification in Windows10'''
    notif = ToastNotifier()
    notif.show_toast("SnapBoard OCR", text)


image_file = 'snap.png'

# img = ImageGrab.grabclipboard()
# img.save(image_file,'PNG')

# text = run_ocr(image_file)

# pyperclip.copy(text)

# print(text)

prev_img = None

while True:
    img = ImageGrab.grabclipboard()
    # print(img)

    if img == None:
        continue

    if compare_img(img, prev_img) == False:
        img.save(image_file,'PNG')
        text = run_ocr(image_file)
        pyperclip.copy(text)
        print(text)
        toast_notif(text)
        prev_img = img


