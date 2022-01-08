from gtts import gTTS
import os 

abc = open('sample.text')
text = abc.read()

language = 'en'

obj = gTTS(text= text,lang=language,slow= False)
obj.save("sample.mp3")

os.system("sample.mp3")
