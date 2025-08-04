'''
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():   
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)
        try:
            print("Recognizing...")
            data = recog.recognize_google(audio)
            print(f"You said: {data}")
            speechtx(data)
            return data.lower()
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
            return ""

def speechtx(x):
    obj = pyttsx3.init()
    voices = obj.getProperty('voices')
    obj.setProperty('voice', voices[1].id)  # Female voice
    obj.setProperty('rate', 150)
    obj.say(x)
    obj.runAndWait()

speechtx("Hi , what are you doing?")

if __name__ == '__main__':
    while True:
        text = sptext()
        if "hello" in text:
            speechtx("Hi, how can I help you?")
            data1 = sptext()

            if "your name" in data1:
                name = "My name is Akif."
                speechtx(name)

            if "open youtube" in data1:
                speechtx("Opening YouTube, sir...")
                webbrowser.open("https://www.youtube.com")

                
                
        elif "stop" in text or "exit" in text:
            speechtx("Okay, exiting now.")
            break
        '''
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os 
import pyjokes

def say():
    os.system(f"say         {text} ")

def sptext():   
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)
        try:
            print("Recognizing...")
            data = recog.recognize_google(audio)
            print(f"You said: {data}")
            return data.lower()
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
            return ""

def speechtx(x):
    obj = pyttsx3.init()
    voices = obj.getProperty('voices')
    obj.setProperty('voice', voices[1].id)  # Female voice
    obj.setProperty('rate', 150)
    obj.say(x)
    obj.runAndWait()

speechtx("Hi, what are you doing?")

if __name__ == '__main__':
    while True:
        text = sptext()

        if "hello" in text:
            speechtx("Hi, how can I help you?")
            data1 = sptext()

            if "your name" in data1:
                speechtx("My name is Akif.")

            if "open youtube" in data1:
                speechtx("Opening YouTube, sir.")            
                webbrowser.open("https://www.youtube.com")

            if "open google" in data1:
                speechtx("Opening Google, sir.")
                webbrowser.open("https://www.google.com")

            if "open annafifoundation" in data1:
                speechtx("Opening annafifoundation, sir.")
                webbrowser.open("https://www.annafifoundation.com")

        elif "stop" in text or "exit" in text:
            speechtx("Okay, exiting now.")
            break
