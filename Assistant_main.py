import webbrowser
import pyttsx3 #helps in speak
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest

#       Engine to Speak
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[4].id)
# print(voices[4])
engine.setProperty("rate",190) # how much fast assistant will speak

#       speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#       Taking user commands function
def take_command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 # gap of 1 sec after printing lisening
        r.energy_threshold = 400 #with how much energy we should speak
        audio = r.listen(source,0,4) # will wait for 4 second then move on to next function

    try:
        print("Understanding ...")
        query =r.recognize_google(audio,language='en-in')
        print(f"You said {query}\n")
    except Exception as e:
        print("wait a minute..")
        return "None"
    return query

#Creating an alarm function
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")

#Password function
for i in range(3):
    a = input("Enter password to open your assistant : - ")
    pw_file = open("Password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("Welcome ! PLZ SPEAK [ WAKE UP SUNDAY ] to load me up")
        break
    elif(i ==2 and a!= pw):
        exit()
    elif(a!=pw):
        print("Try Again")

# from GUI import play_gif
# play_gif()

# Main program starts from here ----------------------------------------------------------------
speak("Installing required packages")

if __name__ == '__main__':
    while True:
        query = take_command().lower()
        if "wake up sunday" in query or "sunday wake up" in query:
            from Greet_me import greet_me
            greet_me()

            while True:
                query = take_command().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break

                #----------------------------------------------
                elif "change password" in query:
                    speak("what's the new password")
                    new_pw = input("Enter the new password - ")
                    new_password = open("Password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"your new password is {new_pw}")

                #-------------------------------------
                elif "schedule my day" in query:
                    tasks = [] #Empty list
                    speak("Do you want to clear old tasks (Plz speak yes or no)")
                    query = take_command().lower()
                    if "yes" in query:
                        file = open("Tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks - "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task - "))
                            file = open("Tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        no_tasks = int(input("Enter the no. of tasks - "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task - "))
                            file = open("Tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    speak("Okay sir, here is your schedule")
                    file = open("Tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("Notification.mp3")
                    mixer.music.play()

                    notification.notify(
                        title = "My schedule :- ",
                        message = content,
                        timeout = 15
                    )
                #-------------------------------------------------

                elif "open" in query: #easy methode by writing in search bar
                    query =query.replace("sunday","")
                    query =query.replace("open","")
                    speak("Launching sir")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                    speak(f"{query} successfully launched")
                #-----------------------------------------------------------

                #It takes some time to calculate the nternet speed
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576    #MB = 1024*1024 bytes
                    download_net = wifi.download()/1048576
                    print(f"Wifi upload speed - {upload_net}")
                    print(f"Wifi download speed - {download_net}")
                    speak(f"Wifi uplaod speed - {upload_net}")
                    speak(f"Wifi download speed - {download_net}")


                #=============================================================
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                #-----------------------------------------------
                elif "google" in query:
                    from SearchOnNet import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchOnNet import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchOnNet import searchWikipedia
                    searchWikipedia(query)
                #-----------------------------------------------
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                #-----------------------------------------------
                elif "calculate" in query:
                    from CalculateNumbers import wolfRamAlpha
                    from  CalculateNumbers import calculator
                    query = query.replace("calculate","")
                    query = query.replace("sunday","")
                    calculator(query)

                #-----------------------------------------------
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                #-----------------------------------------------
                elif "what is your name" in query:
                    speak("My name is Sunday and i am your voice assistant, please tell me how can i help you ?")
                elif "hello" in query or "hay" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query or "i am good" in query:
                    speak("That's great, sir")
                elif "how are you" in query or "how r you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query or "thank u" in query:
                    speak("You are welcome, sir")

                elif "tired" in query or "sad" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=cqFqF5aoQBY")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=D5d5xinZI3E")

                #-----------------------------------------------
                elif "play" in query:
                    pyautogui.press("space")
                    speak("played")
                elif "pause" in query:
                    pyautogui.press("space")
                    speak("paused")
                elif "mute" in query or "unmute" in query:
                    pyautogui.press("m")
                    speak("Okay")
                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Truning volume up")
                    volumeup()
                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Truning volume down")
                    volumedown()
                elif "full volume" in query:
                    from Keyboard import volumefull
                    speak("Truning volume to max")
                    volumefull()
                #-----------------------------------------------
                elif "temperature" in query:
                    search = "temperature in gwalior"
                    url = f"https://www.google.com/search?q={search}"
                    r =requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")

                # elif "weather" in query:
                #     search = "weather in gwalior"
                #     url = f"https://www.google.com/search?q={search}"
                #     r =requests.get(url)
                #     data = BeautifulSoup(r.text,"html.parsel")
                #     temp = data.find("div",class_ = "BNeawe").text
                #     speak(f"current {search} is {temp}")
                #-----------------------------------------------
                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")
                #-----------------------------------------------

                #----------- Not Working -----------------------
                elif "set an alarm" in query:
                    print("Input time example:- 10 and 10 and 10")
                    speak("set the time")
                    a = input("Please tell the time: - ")
                    alarm(a)
                    speak("Done, sir")
                #-----------------------------------------------
                # elif "set reminder" or "set a reminder" in query:
                #     reminder = query.replace("set reminder","")
                #     reminder = query.replace("set a reminder","")
                #     speak("You told me" + reminder)
                #     message = open("Reminder.txt","a")
                #     message.write(reminder)
                #     message.close()
                #
                # elif "is there any reminder" in query:
                #     message = open("Reminder.txt","r")
                #     speak(f"You told me to reminder you that {message.read()}")
                #-----------------------------------------------

                elif "shutdown system" in query:
                    speak("Are you sure you want to shurtdown ?")
                    shutdown = input("Do you wish to shutdown your computer ? (yes/no)")

                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown =="no":
                        break


                elif "turn off" in query or "power off" in query:
                    speak("Thank you for your time, Shutting down.")
                    exit()


                #-----------------------------------------------


            # break
