# import Google Text To Speech and Playsound
from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
language='en'
value=input("Enter the Text that you want to listen: ")
speech=gTTS(text=value,lang=language)
speech.save(audio)
playsound(audio)
print("Audio Executed....")