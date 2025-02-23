import pyttsx3
import speech_recognition as sr 
import webbrowser 
import datetime
import pyjokes 

def sptext():
    recog=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining !")
        recog.adjust_for_ambient_noise() 