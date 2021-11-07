import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.karen')
    engine.say(command)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.4)
            spoken_audio = recognizer.listen(mic)
            spoken_text = recognizer.recognize_google(spoken_audio)
            return spoken_text
    except:
        return "Sorry, I didn\'t understand"
