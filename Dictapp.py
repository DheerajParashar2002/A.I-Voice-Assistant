import os
import webbrowser
import pyautogui
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[4].id)
engine.setProperty("rate",190) # how much fast assistant will speak

#       speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd",
           "paint":"mspaint",
           "word":"winword",
           "excel":"excel",
           "chrome":"chrome",
           "vscode":"code",
           "vlc": "vlc",
           "spotify": "spotify",
           "notepad": "notepad",
           "calculator": "calc",
           "powerpoint":"powerpnt"}

def openappweb(query):
    speak("Launching,Sir")
    if ".com" in query or ".com.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"http://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("All tab closed")
    elif "2 tab" in query or "two tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tab closed")
    elif "3 tab" in query or "three tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tab closed")
    elif "4 tab" in query or "four tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tab closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
