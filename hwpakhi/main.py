try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = True
    print("Error pls install pyttsx3 in your VS code")

import speech_recognition as sr
from deep_translator import GoogleTranslator
from googletrans import Translator 
import time
from gtts import gTTS
from playsound import playsound
import pygame

def display_language():
    print("🔸AVAILABLE LANGUAGES🔸:")
    print("1.Hindi:(hi)")
    print("2.Tamil:(ta)")
    print("3.Telegu:(te)")
    print("4.Bengali:(bn)")
    print("5.Marathi:(mr)")
    print("6.Gujrati:(gu)")
    print("7.Malayalam:(ml)")
    print("8.Punjabi:(pa)")

    choice = input("✨please select the target language number(1-8)✨: ")
    language_dict = {
        "1":"hi",
        "2":"ta",
        "3":"te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }

    return language_dict.get(choice,"es")
language = display_language()
print(language)

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🔹please speak now in english....")
        audio = recognizer.listen(source)
    print("🎀recognizing speech🎀")
    text = recognizer.recognize_google(audio,language="en-US")
    print("✨audio detected is:")
    return text
text = speech_to_text()
print(text)

translated = GoogleTranslator(source='auto', target=language).translate(text)
print(translated)
tts = gTTS(text=translated,lang=language)
tts.save("output.mp3")

pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(0.5)
# it was actually just translating into hindi so i with the help of ai slightly changed the code and now it will actually translate the selected options