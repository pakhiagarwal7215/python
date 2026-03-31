import queue
import sounddevice as sd
from vosk import Model,KaldiRecognizer
import pyttsx3
import json
import datetime
model = Model("model")
recoginizer = KaldiRecognizer(model,16000)
audio_queue = queue.Queue()
tts_engine = pyttsx3.init()
def callback(indata,frames,time,status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))
def process_query(query):
    query = query.lower()
    
    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}."
    elif "date" in query:
        day = datetime.datetime.now().strftime("%B %d,%Y")
        return f"Today's date is {day}"
    elif "hello" in query:
        return"Hi🎀, to know the current time say time and to know the date say date"
    elif"change username to" in query:
        username = query.lower()
        return f"Username changed to :{username}"
    else:
        return f"i don't understand"
with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1, 
        callback=callback
):
    print("hi there , say 'hello', 'date', 'time' is you want a specific user name you'll prefer me to call you, just say 'change username to' and the desired name!")

    while True:
        data = audio_queue.get()
        if recoginizer.AcceptWaveform(data):
            result = json.loads(recoginizer.Result())
            text = result.get("text","")
            if text:
                print(" you said this:",text)
                response = process_query(text)
                print("Assistant:", response)
                tts_engine.say(response)
                tts_engine.runAndWait()
# hello this is a note from pakhi :
# i added a few more lines to the code so that it can ask and reply when