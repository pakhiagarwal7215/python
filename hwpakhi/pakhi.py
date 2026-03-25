try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("Error pls install pyttsx3 in your vs code")
import speech_recognition as sr
from deep_translator import GoogleTranslator
from googletrans import Translator # Google Translate API
import time
from gtts import gTTS
from playsound import playsound
import pygame



# Step 1: Display language options and get user's choice
def display_language_option():
    print("???? Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    # User selects language
    choice = input("Please select the target language number (1-8): ")

    language_dict = {
                        "1": "hi",
                        "2": "ta",
                        "3": "te",
                        "4": "bn",
                        "5": "mr",
                        "6": "gu",
                        "7": "ml",
                        "8": "pa"
}
    return language_dict.get(choice, "es")
language=display_language_option()
print(language)


# step2:speech to text: recognises  what you say and types it
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Please speak now in English...")
        audio = recognizer.listen(source)
    print("=======recognizing speech=========")
    text = recognizer.recognize_google(audio,language="en-US")
    print("you said this:",text)
    return text
text = speech_to_text()
print(text)


# Step 3: Translate to selected target language
translated = GoogleTranslator(source='auto', target='hi').translate(text)
print(translated)


# step4 : speaking the translated text
#engine = pyttsx3.init()
#engine.setProperty('rate',150)
#voices = engine.getProperty('voices')
# Print voices (debug once)
#for v in voices:
   # print(v.id)

# Always use a valid available voice
#engine.setProperty('voice', voices[0].id)

#engine.say(translated)
#engine.runAndWait()

tts = gTTS(text=translated, lang=language)
tts.save("output.mp3")

pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.5)