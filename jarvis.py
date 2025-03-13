import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():   
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!")
        recog.adjust_for_ambient_noise(source)  
        audio = recog.listen(source)
        try:
            print("Recognizing...")
            data = recog.recognize_google(audio)
            #print(data)
            return data
        except sr.UnknownValueError:
            print("Could not understand the audio")

#sptext()
def speechtx(x):
    obj=pyttsx3.init()
    voice=obj.getProperty('voices')
    obj.setProperty('voice',voice[1].id)
    rate=obj.getProperty('rate')
    obj.setProperty('rate',150)
    obj.say(x)
    obj.runAndWait()

#speechtx("Hii bro what r u doing ")

if __name__=='__main__':
        #if sptext().lower() =="hello":
           data1=sptext().lower()
           print(data1)
           if "your name"in data1:
                name="my name is akif"
                speechtx(name)
           
        