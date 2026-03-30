import speech_recognition as sr # speech-text
import pyttsx3 #text-speech
from datetime import datetime # gets current date and time
def speak(text):
    engine = pyttsx3.init()# initializes the text to speech module
    engine.setProperty('rate',150)#150 words per minute max
    engine.say(text)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:# uses microphone as the source
        print("🔴listening, speak now....")
        audio = r.listen(source)# starts listenining
        try:
            command = r.recognize_google(audio)# uses google to recognize audio
            print(f"you said {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("could not understand what you said")
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



if __name__=="__main__":
    speak("voice assistant activated")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break
        