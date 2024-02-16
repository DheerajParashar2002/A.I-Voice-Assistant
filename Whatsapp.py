import pyttsx3
import speech_recognition
import pywhatkit
import datetime
import webbrowser
import os
from bs4 import BeautifulSoup
from time import  sleep
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)
engine.setProperty("rate", 190)  # how fast the assistant will speak


# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 # gap of 1 sec after printing lisening
        r.energy_threshold = 300 #with how much energy we should speak
        audio = r.listen(source,0,4) # will wait for 4 second then move on to next function

    try:
        print("Understanding ...")
        query =r.recognize_google(audio,language='en-in')
        print(f"You said {query}\n")
    except Exception as e:
        print("Say that again..")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes= 2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message")
    a = int(input('''Person 1 - 1
                     Person 2 - 2'''))
    if a == 1:
        speak("What is your message")
        message = str(input("Enter the message - "))
        pywhatkit.sendwhatmsg("+919457822828",message,time_hour=strTime,time_min=update)
    elif a== 2:
        speak("What is your message")
        message = str(input("Enter the message - "))
        pywhatkit.sendwhatmsg("+917697005684", message, time_hour=strTime, time_min=update)




