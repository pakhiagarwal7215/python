import speech_recognition as sr
import pyttsx3
from datetime import datetime
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now....")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)# uses google to recognize audio
            print(f"you said {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
    return ""
def respond_to_command(command):
    speak(f"inside the response you said {command}")
    if "hello" in command:
        speak("Hi user! how can i help you today")
    elif "hi" in command:
        speak("Hi user! how can i help you today")
    elif "your name" in command:
        speak("I am your python voice assistant🎀")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"the time is {now}")
    elif "date" in command:
        today = datetime.now().strftime("%d-%M-%Y")
        speak(f"The date is {today}")
    elif "exit" in command or "stop" in command:
        speak("Farewell user, goodbye!")
        return False
    else:
        speak("i am not sure how to help you")
    return True
if __name__ == "__main__":
    speak("Voice assistant activated")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break