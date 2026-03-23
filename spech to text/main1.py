import threading
import sys
import pyaudio
import numpy as np
import time
import speech_recognition as sr
from speech_recognition import AudioData
stop_event = threading.Event()
def wait_for_enter():
    input()
    stop_event.set()
def record_audio(label):
    stop_event.clear()
    p = pyaudio.PyAudio()
    stream = p.open(format= pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024)
    frames = []
    print("Press enter to stop")
    threading.Thread(target=wait_for_enter,daemon=True).start()
    print("recording started for ",label)
    while not stop_event.is_set():
        frames.append(stream.read(1024, exception_on_overflow=False))
        print(".", end="", flush=True)
    print(" Done!")

    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()

    return b''.join(frames), 16000, width

def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)

    return {
        'duration':len(samples) / rate,
        'avg_volume': np.mean(np.abs(samples)),
        'max_volume': np.max(np.abs(samples)),
        'samples': samples
    }
def convert_to_text(data,rate,width):
    recognizer = sr.Recognizer()
    audio = AudioData(data,rate,width)
    text = recognizer.recognize_google(audio)
    print(f"📝 Transcription: {text}")

print("=" * 40)
print("VOICE ANALYSIS LAB")
print("=" * 40)

# Recording 1
audio1, rate, width = record_audio("Recording 1: Speak normally")
audio2, rate2, width2 = record_audio("Recording 2: Speak a bit more loudly")
stats1 = analyze_audio(audio1, rate)
stats2 = analyze_audio(audio2, rate2)
text1 = convert_to_text(audio1, rate, width)
print(f"text1 = {text1}")
text2 = convert_to_text(audio2, rate, width)
print(f"text2 = {text2}")
print("\n" + "=" * 40)
print("COMPARISON RESULTS")
print("=" * 40)

# Avoid division by zero
if stats2['duration'] == 0 or stats1['duration'] == 0:
    print("Cannot compare duration (zero length recording)")
else:
    if stats1['duration']>stats2["duration"]:
        print("Recording 1 is longer by ",stats1['duration'] - stats2['duration'])
    else:
        print("recording 2 is longer by ", stats2['duration']-stats1['duration'])
if stats2['avg_volume'] == 0 or stats1['avg_volume'] == 0:
    print("Cannot compare volume (silent recording)")
else:
    if stats1['avg_volume'] > stats2['avg_volume']:
        
        diff = ((stats1['avg_volume'] - stats2['avg_volume']) / stats2['avg_volume']) * 100
        print(f"Recording 1 is louder by {diff:.1f}%")
    else:
        diff = ((stats2['avg_volume'] - stats1['avg_volume']) / stats1['avg_volume']) * 100
        print(f"Recording 2 is louder by {diff:.1f}%")
