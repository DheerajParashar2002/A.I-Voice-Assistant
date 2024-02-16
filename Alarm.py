import pyttsx3
import datetime
import os

#  --------------------Not Working -------------------------

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[4].id)
engine.setProperty("rate",190) # how much fast assistant will speak

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("alarm","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime  == Alarmtime:
            speak("Alarm ringing, Sir")
            os.startfile("ring 1.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)
