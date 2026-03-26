import threading
import sys
import pyaudio
import numpy as np
import time
import wave
import speech_recognition as sr
from speech_recognition import AudioData
import matplotlib.pyplot as mp
stop_event = threading.Event()

def wait_for_enter():
    input()
    stop_event.set()

def record_audio():
    stop_event.clear()
    p = pyaudio.PyAudio()
    stream = p.open(format= pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024)
    frames=[]
    print("Press enter to stop")
    threading.Thread(target=wait_for_enter,daemon=True).start()
   
    while not stop_event.is_set():
        frames.append(stream.read(1024,exception_on_overflow=False))
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames),16000,width
def save_audio(data,rate,width,filename="recording.wav"):
    with wave.open(filename,'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"💾 Saved: {filename}")  
def convert_to_text(data,rate,width):
    recognizer = sr.Recognizer()
    audio = AudioData(data,rate,width)
    text = recognizer.recognize_google(audio)
    print(f"📝 Transcription: {text}")
def plot_waveform(data,rate):
    samples = np.frombuffer(data, dtype=np.int16)
    time_axis = np.linspace(0, len(samples) / rate, len(samples))
    mp.plot(time_axis,samples,color = "red")
    mp.title("Your Voice Waveform")
    mp.xlabel("Time (seconds)")
    mp.ylabel("Amplitude")
    mp.grid(True, alpha=0.3)
    mp.tight_layout()
    mp.show()
if __name__ =="__main__":
    print("speak into your microphone")
    audio_data,rate,width=record_audio()
    save_audio(audio_data,rate,width)
    convert_to_text(audio_data,rate,width)
    plot_waveform(audio_data,rate)