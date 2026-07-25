import speech_recognition as sr
import pyaudio

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="ru-RU")
    print(f"You sayed: {text}")
except sr.RequestError:
    print("Error while sending a request to the Google API.")
except sr.UnknownValueError:
    print("Unable to understand what you said.")
