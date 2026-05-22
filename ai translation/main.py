import speech_recognition as sr 
import pyttsx3
from googletrans import Translator
from gtts import gTTS
import os
def speak(text,language="en"):
    tts = gTTS(text=text,lang=language)
    filename = "output.mp3"
    tts.save(filename)
    os.system(f"start {filename}"if os.name == "nt" else f"afplay {filename}")
def stt():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now in english........")
        audio = recognizer.listen(source)
        try:
            print("....Recognizing speech....")
            text = recognizer.recognize_google(audio,language="en-US")
            print(f"You said ={text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"API error:{e}")
        return""
def display_language_options():
    print("🎀Available translation languages=")
    print("1.Hindi(hi)")
    print("2.Tamil(ta)")
    print("3.Telugu(te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    choice = input("Please select the target language number (1-8):")
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
    return language_dict.get(choice,"es")
def translate(text,target_language="es"):
    try:
        translator = Translator()
        translation = translator.translate(text,dest=target_language)
        print(f"translated text = {translation.text}")
        return translation.text
    except Exception as e:
        print("Error : ",e)
text =stt()
target_language = display_language_options()
translated_text = translate(text,target_language)
speak(translated_text)