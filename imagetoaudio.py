import pytesseract
from PIL import Image
import os 
from gtts import gTTS 
img = Image.open('img.jpg')
mytext = pytesseract.image_to_string(img)
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("mpg321 welcome.mp3") 
