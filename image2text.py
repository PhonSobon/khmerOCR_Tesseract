import pytesseract

# Set path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Example usage:
from PIL import Image

img = Image.open('images/test1.jpg')

# custom_config = r'-l khm+eng --oem 3 --psm 6'
# text = pytesseract.image_to_string(img, config=custom_config)

text = pytesseract.image_to_string(img, lang='eng+khm')

print(text)

with open('output2.txt', 'w', encoding='utf-8') as f:
    f.write(text)

