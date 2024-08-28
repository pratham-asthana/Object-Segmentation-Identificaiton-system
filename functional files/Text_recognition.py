#STEP 4 --> Text Recognition 

import pyautogui
import pytesseract
from PIL import Image

#Capturing,saving and opening screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")
image = Image.open("screenshot.png")

#Recognizing Text and converting it to string using pytesseract
text = pytesseract.image_to_string(image)

#Printing the recognized Text.
print("Recognized Text:")
print(text)
