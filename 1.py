# import speech_recognition as sr
import pyttsx3
import speech_recognition as sr

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "Sorry, I did not understand that."
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return "Speech service unavailable."

    return query

if __name__ == '__main__':
        print('VS Code')
        say("Hello, I am mohammed abdul akif ")
        while True:
            print("Listening...")
            text = takeCommand()
            say(text)
